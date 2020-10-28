const app = Vue.createApp({
  data() {
    return {
      todo_lists: [],
      todo_items: [],
      login: '',
      password: '',
      username: ''
    }
  },
  async created() {
    this.load_todo_list();
    this.username = this.username_get();
  },
  methods: {
    username_set(username) {
      this.username = username;
      window.localStorage.setItem('username', username);
    },
    username_get() {
      let username = window.localStorage.getItem('username');
      return username ? username : '';
    },
    username_reset() {
      this.username = '';
      window.localStorage.removeItem('username');
    },
    async load_todo_list() {
      this.todo_lists = await axios.get('/lists')
        .then((r) => { return r.data; })
        .catch((error) => {
          console.log(error);
        });
    },
    async process_login() {
      await axios.post('/login', { login: this.login, password: this.password })
        .then((r) => {
          this.username_set(r.data.name);
          this.login = '';
          this.password = '';
          this.load_todo_list();
        }).catch((error) => {
          console.error(error);
        })
    },
    async process_logout() {
      await axios.get('/logout')
        .then(() => {
          this.username_reset();
          this.todo_lists = [];
          this.todo_items = [];
        }).catch((error) => {
          console.log(error);
        })
    }
  }
})

app.component('todo-lists', {
  methods: {
    async update(id) {
      this.$parent.todo_items = await axios.get(`/lists/${id}/items`)
        .then((r) => { return r.data });
    }
  },
  template: `
    <input id="button_{{ list.id }}" name="lists" type="radio" @click="update(list.id)">
    <label for="button_{{ list.id }}">
      #{{ list.id }} {{ list.title }} by {{ list.owner ? list.owner : "unknown" }}
    </label><br>
  `,
  props: ['list'],
})
app.component('todo-items', {
  template: `
    <p class="items">#[{{ item.id }}, {{ item.todolist }}] {{ item.value }} [{{ item.status }}]</p>
  `,
  props: ['item']
})
app.mount('#todo-list-app')
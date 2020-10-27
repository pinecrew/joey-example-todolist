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
    this.todo_lists = await axios.get('/lists').then((r) => { return r.data; });
    let username = window.localStorage.getItem('username');
    this.username = username ? username : '';
  },
  methods: {
    async process_login() {
      await axios.post('/login', { login: this.login, password: this.password }).then((r) => {
        this.username = r.data.name;
        window.localStorage.setItem('username', r.data.name);
      })
      this.todo_lists = await axios.get('/lists').then((r) => { return r.data; });
    },
    async process_logout() {
      await axios.get('/logout');
      window.localStorage.removeItem('username');
      this.username = '';
      this.todo_lists = [];
      this.todo_items = [];
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
    <p @click="update(list.id)">#{{ list.id }} {{ list.title }} by {{ list.owner ? list.owner : "unknown" }}</p>
  `,
  props: ['list'],
})
app.component('todo-items', {
  template: `
    <p>#[{{ item.id }}, {{ item.todolist }}] {{ item.value }} [{{ item.status }}]</p>
  `,
  props: ['item']
})
app.mount('#todo-list-app')
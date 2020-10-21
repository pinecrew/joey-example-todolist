const app = Vue.createApp({
  data() {
    return {
      todo_lists: [],
      todo_items: []
    }
  },
  async created() {
    this.todo_lists = await axios.get('/lists')
                                 .then((r) => { return r.data; });
  },
})

app.component('todo-lists', {
  methods: {
    async update(id) {
      this.$parent.todo_items = await axios.get(`/lists/${id}/items`)
                                           .then((r) => { return r.data });
    }
  },
  template: `
    <p @click="update(list.id)">#{{ list.id }} by {{ list.owner ? list.owner : "unknown" }}</p>
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
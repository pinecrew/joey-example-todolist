const app = Vue.createApp({
  data() {
    return {
      items: []
    }
  },
})

app.component('todo-item', {
  template: `<li>{{ todo.id }} -- {{ todo.owner }}</li>`,
  props: ['todo'],
})
let todo = app.mount('#todo-list-app')

axios.get('/lists').then(function (r) {
  todo.items = r.data;
});

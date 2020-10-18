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

axios.get('http://192.168.88.250:8000/lists').then(function (r) {
  todo.items = r.data;
});
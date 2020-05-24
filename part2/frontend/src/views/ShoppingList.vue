<template>
  <div class="custom-home">
    <div class="card mt-5">
      <h2 class="card-header">Shopping list</h2>
      <div class="mt-3 ml-3" v-cloak v-if="numItems > 0">
        <p>showing {{numItems}} items</p>
      </div>
      <table class="table table-striped">
        <thead class="thead-light">
          <th>#</th>
          <th>Name</th>
          <th>Quantity</th>
          <th>Missing?</th>
          <th></th>
        </thead>
      <tbody v-cloak>
        <tr v-for="(s_item, index) in shopping_list" :key="index">
          <td>{{index + 1}}</td>
          <td>{{s_item.name}}</td>
          <td>{{s_item.quantity}}</td>
          <td>{{s_item.missing}}</td>
          <td><button class="btn btn-warning" @click="remove(index)">remove</button></td>
        </tr>
      </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'shoppingList',
  data() {
      return {
        shopping_list: []
      }
  },
  created: function () {
      this.fetchList();
  },
  methods: {
      fetchList: function () {
          var url = 'http://localhost:5000/index';
          axios.get(url)
              .then((res) => {
                  this.shopping_list = res.data.shopping_list;
              });
      },
      remove: function (index) {
          this.shopping_list.splice(index, 1);
      },
  }
}
</script>

<style>
  [v-cloak] {
    display: none;
  }
</style>



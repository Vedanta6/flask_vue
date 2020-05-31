<template>
  <div class="custom-home">
    <main role="main" class="inner cover">
      <h3 class="cover-heading">Shopping list
        <v-icon v-blur @click="fetchDefaults" :class="icons[4].class">
          {{ icons[4].icon }}
        </v-icon>
        <v-icon v-blur @click="updateList" :class="icons[5].class">
          {{ icons[5].icon }}
        </v-icon>
      </h3>
      <v-layout justify-center justify-content-center mt-4>
        <v-simple-table fixed-header>
          <template v-slot:default>
            <thead>
              <th></th>
              <th>Name</th>
              <th>Quantity</th>
              <th>Units</th>
              <th style="display: none;">Missing?</th>
              <th></th>
            </thead>
            <tbody v-cloak>
              <tr v-for="(item, index) in shopping_list"
                  :key="index"
              >
                <td>
                  <v-icon v-blur
                          :class="icons_list[index].class"
                          @click="checkRow(index)"
                          v-model="icons_list[index]"
                  >
                    {{ icons_list[index].icon }}
                  </v-icon>
                </td>
                <td>
                  <input class="on-fly-input"
                         v-model="shopping_list[index].name"
                         :style="icons_list[index].style"
                  />
                </td>
                <td>
                  <input class="on-fly-input"
                         type="number"
                         v-model="shopping_list[index].quantity"
                         :style="icons_list[index].style"
                  />
                </td>
                <td>
                  <input class="on-fly-input"
                         v-model="shopping_list[index].unit"
                         :style="icons_list[index].style"
                  />
                </td>
                <td style="display: none;">
                  <input class="on-fly-input"
                         v-model="shopping_list[index].missing"
                         :style="icons_list[index].style"
                  />
                </td>
                <td>
                  <v-icon v-blur
                          @click="removeRow(index)"
                  >
                    {{ icons[2].icon }}
                  </v-icon>
                </td>
              </tr>
              <tr class="no-highlight">
                <td>
                  <v-icon v-blur
                          @click="addRow"
                          :class="icons[3].class"
                  >
                    {{ icons[3].icon }}
                  </v-icon>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-layout>
    </main>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'shoppingList',
    data() {
      return {
        shopping_list: [],
        icons: [
          {
            'icon': 'mdi-checkbox-blank-outline',
            'class': '',
            'style': 'text-decoration:none;color:unset;'
          },
          {
            'icon': 'mdi-checkbox-marked-outline',
            'class': 'v-icon-highlighted',
            'style': 'text-decoration:line-through;color:#adb7bbd1;'
          },
          {
            'icon': 'mdi-close',
            'class': '',
            'style': ''
          },
          {
            'icon': 'mdi-plus',
            'class': 'v-icon-highlighted',
            'style': ''
          },
          {
            'icon': 'mdi-refresh',
            'class': 'v-icon-highlighted pl-1 pb-1',
            'style': ''
          },
          {
            'icon': 'mdi-content-save',
            'class': 'v-icon-highlighted pl-1 pb-1',
            'style': ''
          }
        ],
        icons_list: []
      }
    },

    created: function () {
      this.fetchDefaults();
    },

    beforeRouteLeave: function (to, from, next) {
      this.updateList();
      next();
    },

    methods: {
      fetchDefaults: function () {
        const path = 'http://localhost:5000/shoppinglist';
        axios.get(path)
          .then((res) => {
            this.shopping_list = res.data.shopping_list;
            this.icons_list = [];
            for (var i = 0; i < this.shopping_list.length; i++) {
              if (this.shopping_list[i].missing == true) {
                this.icons_list.push(this.icons[0]);
              } else {
                this.icons_list.push(this.icons[1]);
              }
            }
          })
          .catch((error) => {
            console.error(error);
          });
      },

      updateList: function () {
        const path = 'http://localhost:5000/shoppinglist';
        axios.post(path, this.shopping_list)
          .then(() => {
            this.fetchDefaults();
          })
          .catch((error) => {
            console.log(error);
          });
      },

      removeRow: function (index) {
        this.shopping_list.splice(index, 1);
        this.icons_list.splice(index, 1);
      },

      addRow: function () {
        this.shopping_list.push({
          name: '',
          quantity: 0,
          unit: '',
          missing: true,
        });
        this.icons_list.push(this.icons[0]);
      },

      checkRow: function (index) {
          if (this.icons_list[index].icon == this.icons[0].icon) {
              this.icons_list[index] = this.icons[1];
              this.shopping_list[index].missing = false;
          } else {
              this.icons_list[index] = this.icons[0];
              this.shopping_list[index].missing = true;
          }
      },

      directives: {
        focus: {
          inserted (el) {
            el.focus();
          }
        }
      }

    }
  };
</script>
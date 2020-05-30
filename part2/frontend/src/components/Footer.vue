<template>
  <v-footer
    padless
    absolute
  >
    <v-card
      flat
      tile
      class="text-center"
      style="width:100%;"
    >
      <v-card-text class="text-muted">
        {{ new Date().getFullYear() }} <span>&copy; All rights reserved</span>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

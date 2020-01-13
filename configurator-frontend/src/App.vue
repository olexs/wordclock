<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title class="headline text-uppercase">Wordclock Color</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <v-row>
          <v-col v-if="$vuetify.breakpoint.mdAndUp" md="3" lg="4" />
          <v-col cols="12" lg="4" md="6" align="center">
            <v-color-picker
              hide-mode-switch
              hide-inputs
              width="100%"
              hide-canvas
              :disabled="!loaded"
              v-model="color"
              @input="update"
            />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from "axios";
import qs from 'qs';

export default {
  name: "App",

  components: {},

  data: () => ({
    loaded: false,
    color: {
      r: 255,
      g: 255,
      b: 64,
      a: 0.25
    },
    debounceTimer: 0
  }),

  methods: {
    update() {
      if (this.loaded) {
        if (this.debounceTimer) clearTimeout(this.debounceTimer);

        this.debounceTimer = setTimeout(() => {
          axios.post("/setcolor?" + qs.stringify({
            r: Math.round(this.color.r * this.color.a),
            g: Math.round(this.color.g * this.color.a),
            b: Math.round(this.color.b * this.color.a)
          }));
        }, 200);
      }
    }
  },

  async mounted() {
    const { data } = await axios.get("/getcolor");
    const brightest = Math.max(data.r, data.g, data.b);
    this.color = {
      r: (data.r / brightest) * 255,
      g: (data.g / brightest) * 255,
      b: (data.b / brightest) * 255,
      a: brightest / 255
    };
    this.loaded = true;
  }
};
</script>

<template>
  <div class="home container py-3">
    <template v-if="$store.state.isAuthenticated">
        <div class="columns is-centered">
          <div class="column is-9-fullhd is-10-desktop is-10-tablet is-10-mobile
          has-text-centered-mobile py-5 is-offset-1-mobile">
            <router-link to="/sync" class="button is-link is-fullwidth-mobile">
              + Sync more channels
            </router-link>
          </div>
        </div>
        <div class="columns is-centered is-mobile">
          <div class="column is-9-fullhd is-10-desktop is-10-tablet is-9-mobile">
            <div class="columns is-mobile">
              <div class="column is-2-desktop is-3-tablet is-7-mobile">
                <span class="is-12 has-text-success">Source:</span>
              </div>
            </div>
          </div>
        </div>
        <div class="columns is-centered is-mobile">
          <div class="column is-9-fullhd is-10-desktop is-10-tablet is-9-mobile">
            <div class="columns is-mobile">
              <div class="column is-2-desktop is-3-tablet is-7-mobile">
                <select class="is-12 dropdown-content" v-model="generate_from">
                  <option v-for="generator_option in generate_from_options"
                  :key="generator_option.value" :value="generator_option.value">
                    {{ generator_option.text }}
                  </option>
                </select>
              </div>
            </div>
          </div>
        </div>
        <form @submit.prevent="submitForm" class="has-background-info">
        <div class="columns is-multiline is-centered is-mobile">
            <div class="column is-9-fullhd is-10-widescreen is-10-desktop is-10-tablet
            is-11-mobile py-6">
                    <div class="notification" v-if="errors.length">
                        <p v-for="error in erros" v-bind:key="error">
                          {{ error }}
                        </p>
                    </div>
                    <div class="columns is-centered is-mobile is-hidden-tablet">
                      <div class="column is-10-mobile is-6-tablet is-6-desktop ">
                        <div class="field">
                            <div class="control">
                                <button class="button is-fullwidth is-success">
                                  Generate Inspiration
                                </button>
                            </div>
                        </div>
                      </div>
                    </div>
                    <div class="columns is-centered is-multiline">
                      <div
                        class="column is-6-desktop is-6-tablet is-10-mobile is-offset-1-mobile"
                        v-for="video in video_detail"
                        v-bind:key="video.id"
                      >
                        <a href="#" @click.prevent="guess(video.id, video.view_count)">
                        <div class="box has-background-link media-center video-detail-box">
                          <figure class="image image is-16by9">
                            <img :src="video.thumbnail_url" alt="thumbnail">
                            <div class="centered">Centered</div>
                          </figure>
                          <br>
                          <div class="box video-detail-box has-background-link-light">
                            <h1>{{ video.title }}</h1>
                          </div>
                        </div>
                        </a>
                      </div>
                    </div>
                    <div class="columns is-centered is-hidden-mobile">
                      <div class="column is-6-mobile is-6-tablet is-6-desktop ">
                        <div class="field">
                            <div class="control">
                                <button class="button is-fullwidth is-success">
                                  Generate
                                </button>
                            </div>
                        </div>
                      </div>
                    </div>
            </div>
        </div>
        </form>
    </template>

    <template v-else>
        <div class="columns">
            <div class="column is-3-fullhd is-3-desktop is-10-tablet is-offset-4-desktop
            is-offset-1-tablet is-12-mobile py-6">
                <form @submit.prevent="submitForm">
                    <div class="notification" v-if="errors.length">
                        <p
                            v-for="error in erros"
                            v-bind:key="error"
                        >
                            {{ error }}
                        </p>
                    </div>
                    <div class="columns is-multiline-mobile is-centered">
                      <div
                        class="column is-12-desktop is-one-third-tablet is-10-mobile
                        is-offset-1-mobile"
                        v-for="video in video_detail"
                        v-bind:key="video.id"
                      >
                        <a href="#" @click.prevent="guess(video.id, video.view_count)">
                        <div class="box has-background-link media-center video-detail-box">
                          <figure class="image image is-16by9">
                            <img :src="video.thumbnail_url" alt="thumbnail">
                          </figure>
                          <br>
                          <div class="box video-detail-box has-background-link-light">
                            <h1>{{ video.title }}</h1>
                          </div>
                        </div>
                        </a>
                      </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-fullwidth is-success">
                              Generate
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Play',
  data() {
    return {
      errors: [],
      video_detail: [],
      most_views: 0,
      generate_from: 'SYNCED',
      video_quantity: 'TWO',
      generate_from_options: [
        { text: 'synced channels', value: 'SYNCED' },
        { text: 'random channels', value: 'RANDOM' },
        { text: '50/50', value: 'RAN_SYNC' },
      ],
      video_quantity_options: [
        { text: '1', value: 'ONE' },
        { text: '2', value: 'TWO' },
        { text: '3', value: 'THREE' },
        { text: '4', value: 'FOUR' },
      ],
    };
  },
  mounted() {
    this.submitForm();
  },
  methods: {
    submitForm(e) {
      axios
        .get('api/v1/generator/', {
          params: {
            generate_from: this.generate_from,
            video_quantity: this.video_quantity,
          },
        })
        .then((response) => {
          this.most_views = 0;
          if (response.data) {
            this.video_detail = [];
            for (let i = 0; i < response.data.length; i += 1) {
              this.video_detail.push(response.data[i]);
              if (this.video_detail[i].view_count > this.most_views) {
                this.most_views = this.video_detail[i].view_count;
              }
            }
          }
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              if (error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`);
              }
            }
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            console.log(JSON.stringify(error.message));
          } else {
            console.log(JSON.stringify(error));
          }
        });
    },
    guess(id, views) {
      if (views < this.most_views) {
        console.log('Wrong');
      } else {
        console.log('Correct');
      }
    },
  },
};
</script>

<style lang="scss">
@import 'mystyles.scss';

</style>

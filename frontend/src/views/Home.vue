<template>
  <div class="home">
    <template v-if="$store.state.isAuthenticated">
      <div class="container py-3">
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
              <div class="column is-1 is-1-tablet is-5-mobile is-3-mobile pb-0 mb-0">
                <span class="has-text-success">Quantity:</span>
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
              <div class="column is-1-desktop is-1-tablet is-3-mobile">
                <select class="is-12 dropdown-content px-5" v-model="video_quantity">
                  <option v-for="quantity in video_quantity_options"
                  :key="quantity.value" :value="quantity.value">
                    {{ quantity.text }}
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
                    <template v-if="video_detail.length > 0">
                    <div class="columns is-centered is-multiline">
                      <div
                        class="column is-6-desktop is-6-tablet is-10-mobile
                        is-offset-1-mobile"
                        v-for="video in video_detail"
                        v-bind:key="video.id"
                      >
                      <template v-if="video.added === false">
                        <button class="button is-warning is-light is-small mb-1"
                        @click.prevent="storeInCollection(video.id, video)">
                          + Add to collection
                        </button>
                      </template>
                      <template v-else>
                       <button class="button is-warning is-light is-small mb-1 no-click">
                          Added
                        </button>
                      </template>

                        <a target="_blank" :href="`https://www.youtube.com/watch?v=${video.youtube_video_id}`">
                        <div class="box has-background-link media-center video-detail-box-home">
                          <figure class="image is-16by9">
                            <img :src="video.thumbnail_url" alt="thumbnail">
                          </figure>
                          <br>
                          <div class="box has-background-link-light">
                            <h1>{{ video.title }}</h1>
                            <br>
                            <p class="has-text-right is-size-7 view-count-location">
                              <strong>{{ video.view_count }}</strong>
                            </p>
                          </div>
                        </div>
                        </a>
                      </div>
                    </div>
                    </template>
                    <div class="columns is-centered is-hidden-mobile pt-2 mt-2">
                      <div class="column is-6-mobile is-6-tablet is-6-desktop ">
                        <div class="field">
                            <div class="control">
                                <button class="button is-fullwidth is-success">
                                  Generate Inspiration
                                </button>
                            </div>
                        </div>
                      </div>
                    </div>
            </div>
        </div>
        </form>
      </div>
    </template>

    <template v-else>
      <section class="hero is-medium is-info">
        <div class="hero-body">
          <p class="title">
            YouTube Video Idea Generator
          </p>
          <p class="subtitle">
            <router-link to="/sign-up">
              Get Inspiration for your YouTube videos.
            </router-link>
          </p>
          <p class="subtitle">
            <router-link to="/sign-up" class="button is-danger is-rounded">
              Sign up here
            </router-link>
          </p>
        </div>
      </section>
      <section class="hero is-large is-info sync_image_container">
        <div class="hero-body my-0 has-text-right">
          <p class="title">
            Sync
          </p>
          <p class="subtitle">
            <router-link to="/sign-up">
             Synchronise your favourite channels for inspiration.
            </router-link>
          </p>
          <p class="subtitle">
            <router-link to="/sign-up" class="button is-danger is-rounded">
              Sign up here
            </router-link>
          </p>
        </div>
      </section>
      <section class="hero is-large is-info">
        <div class="hero-body py-6">
          <p class="title">
            Inspire
          </p>
          <p class="subtitle">
            <router-link to="/sign-up">
              Get Inspiration for your YouTube videos.
            </router-link>
          </p>
          <p class="subtitle">
            <router-link to="/sign-up" class="button is-danger is-rounded">
              Sign up here
            </router-link>
          </p>
        </div>
      </section>
      <section class="hero is-large is-info home_image_container">
        <div class="hero-body">
          <p class="title">
          </p>
          <p class="subtitle">
            <router-link to="/sign-up">
            </router-link>
          </p>
          <p class="subtitle">
            <br><br><br><br><br><br><br><br>
          </p>
        </div>
      </section>
      <section class="hero is-large is-info">
        <div class="hero-body py-6">
          <p class="title">
            Play
          </p>
          <p class="subtitle">
            <router-link to="/sign-up">
              Get an intuitive understanding of good thumbnails via this mini game
            </router-link>
          </p>
          <p class="subtitle">
            <router-link to="/sign-up" class="button is-danger is-rounded">
              Sign up here
            </router-link>
          </p>
        </div>
      </section>
      <section class="hero is-large is-info play_image_container">
        <div class="hero-body">
          <p class="title">
          </p>
          <p class="subtitle">
            <router-link to="/sign-up">
            </router-link>
          </p>
          <p class="subtitle">
            <br><br><br><br><br><br><br><br>
          </p>
        </div>
      </section>
    </template>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      errors: [],
      video_detail: [],
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
          if (response.data) {
            this.video_detail = [];
            for (let i = 0; i < response.data.length; i += 1) {
              this.video_detail.push(response.data[i]);
              this.video_detail[i].added = false;
              this.video_detail[i].view_count = this.video_detail[i].view_count.toLocaleString();
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
    storeInCollection(id, video) {
      const index = this.video_detail.indexOf(video);
      if (index > -1) {
        this.video_detail[index].added = true;
      }
      axios
        .post('api/v1/video/', { id })
        .then((response) => {
          console.log(response);
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
  },
};
</script>

<style lang="scss">
@import 'mystyles.scss';
.no-click {pointer-events: none;}
.video-detail-box-home {
    height: 95%;
}
</style>

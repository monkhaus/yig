<template>
  <div class="about">
    <div class="columns is-centered py-6">
      <div class="column is-12">
        <div class="columns is-centered">
          <div class="column is-8">
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <a href="https://www.youtube.com/channel/UCNajC7dxZrjTw4lBWWJYZ8w"
                    target="_blank">
                    <figure class="image is-128x128 is-tablet">
                      <img class="is-rounded"
                      src="https://yt3.ggpht.com/ytc/AKedOLRQisT4s78NJCWTiRju8P5o5ATuzWcj5Bc7GTa9Tg=s600-c-k-c0x00ffffff-no-rj-rp-mo"
                      alt="Placeholder image">
                    </figure>
                    </a>
                  </div>
                  <div class="media-content">
                    <div class="media">
                      <a href="https://twitter.com/MonkhouseTom" target="_blank">
                        <div class="media-left mr-5">
                          <figure class="image is-32x32">
                            <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Twitter_colored_svg-512.png"
                            alt="Placeholder image">
                          </figure>
                        </div>
                      </a>

                     <a href="https://www.youtube.com/channel/UCNajC7dxZrjTw4lBWWJYZ8w" target="_blank">
                      <div class="media-left">
                          <figure class="image is-32x32">
                            <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Youtube_colored_svg-512.png"
                            alt="Placeholder image">
                          </figure>
                        </div>
                     </a>
                    </div>
                    <div class="media-content">
                      <p class="subtitle is-6">
                        Hey I'm Tom. I made this website so I can more easily get inspiration
                        for creating content on YouTube. If you'd like to contact me
                        I recommend doing it via YouTube with this link
                        <a target="_blank" href="https://www.youtube.com/channel/UCNajC7dxZrjTw4lBWWJYZ8w/about">here.</a>
                      </p>
                    </div>
                  </div>
                </div>
                <div class="content">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  Phasellus nec iaculis mauris. <a>@bulmaio</a>.
                  <a href="#">#css</a> <a href="#">#responsive</a>
                  <br>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from 'axios';

export default {
  name: 'LogIn',
  data() {
    return {
      errors: [],
    };
  },
  methods: {

  },
};
</script>

<style lang="scss">
@import 'mystyles.scss';
.twitter-link:hover {
  text-decoration: underline;
}
</style>

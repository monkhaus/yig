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
                  I recommend clicking <a href="#">here</a> to see how this application
                  works.
                  <br><br>
                   Sometimes as a content creator inspiration for new videos can run dry.
                   For this reason I decided to make a small web application which helps
                   you come up with <i>new</i> video ideas when you need them. The way I see it,
                   almost no video idea is <strong>unique</strong> &nbsp; - no matter what
                   you think up, someone has probably already created a similar video.
                   <a href="#">HowItWorks</a>
                   <br><br>
                   The premise of this web application is as folllows:<br>
                   I know as a content creator thate there are some channels which are similar
                   to mine. This application allows us to sync those channels in one place
                   and generate inspiration from their content.
                   <br><br>
                   Something I want to just address here is that the goal is not to steal content
                   from creators. It's to synchronise various channels which are similar
                   to yours in one place to help inspire you to come up with new content.
                  <a href="#">HowItWorks</a>
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
  name: 'How',
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

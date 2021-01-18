<template>
  <div>
    <img
      :src="require('@/assets/images/2279730.jpg')"
      style="height: 99vh; width: 100vw; z-index: 0;"
    />
    <div id="login-btn-panel">
      <div>
        <form method="POST" @submit.prevent="handleSubmit">
          <div class="form-group">
            <input
              type="email"
              placeholder="Email"
              class="form-control"
              v-model="email"
              name="username"
            />
          </div>
          <div class="form-group">
            <input
              type="password"
              placeholder="Password"
              class="form-control"
              v-model="password"
              name="password"
            />
          </div>
          <div class="form-group" style="text-align: center;">
            <button class="btn btn-success" type="submit">
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { mapState, mapActions } from "vuex";
import VueToast from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";
Vue.use(VueToast);

export default {
  data() {
    return {
      email: "",
      password: "",
      submitted: false
    };
  },
  computed: {
    ...mapState("account", ["status"])
  },
  created() {
    this.logout();
  },
  watch: {
    status() {
      if (this.status.loginFailed == true) {
        Vue.$toast.open({
          message: "Login Failed. Please check your account!",
          type: "error",
          duration: 4000
        });
      }
    }
  },
  methods: {
    ...mapActions("account", ["login", "logout"]),
    handleSubmit(e) {
      this.submitted = true;
      const { email, password } = this;
      if (email && password) {
        this.login({ email, password });
      }
    }
  }
};
</script>

<style scoped>
#login-btn-panel {
  z-index: 0;
  position: absolute;
  bottom: 12%;
  left: 8%;
  height: 30%;
  width: 23%;
}
#login-btn-panel input {
  font-size: 20px !important;
  width: 100%;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 10px;
  color: #433d45;
  background-color: white;
}
#login-btn-panel button {
  font-size: 20px !important;
  width: 100%;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 10px;
}
</style>

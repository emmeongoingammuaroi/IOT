import { userService } from "../../services";
import router from "../../router";

const user = JSON.parse(localStorage.getItem("user"));
const state = user
  ? { status: { loggedIn: true, loginFailed: false }, user }
  : { status: { loginFailed: false }, user: null };

const actions = {
  login({ dispatch, commit }, { email, password }) {
    userService.login(email, password).then(
      user => {
        commit("loginSuccess", user);
        router.push("/");
      },
      error => {
        commit("loginFailure", error);
        //dispatch("alert/error", error, { root: true });
      }
    );
  },
  logout({ commit }) {
    userService.logout();
    commit("logout");
  }
};

const mutations = {
  loginSuccess(state, user) {
    state.status = { loggedIn: true, loginFailed: false };
    state.user = user;
  },
  loginFailure(state) {
    state.status = { loginFailed: true };
    state.user = null;
  },
  logout(state) {
    state.status = { loginFailed: false };
    state.user = null;
  }
};

export const account = {
  namespaced: true,
  state,
  actions,
  mutations
};

const state = {
  time: [],
  temperature: [],
  humidity: [],
  gas: []
};

const mutations = {
  addNewSpec(state, spec) {
    state.time.push(new Date().toLocaleTimeString());
    state.temperature.push(spec.temperature);
    state.humidity.push(spec.humidity);
    state.gas.push(spec.gas);
  },
  clearSpecs(state) {
    state.temperature = [];
    state.humidity = [];
    state.gas = [];
  }
};

export const spec = {
  namespaced: true,
  state,
  mutations
};

import config from "../config";
import { authHeader } from "./authHeader";

export const userService = {
  login,
  logout,
  getSpecs,
  publish
};

function login(email, password) {
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  };

  return fetch(`${config.apiUrl}/login/`, requestOptions)
    .then(handleResponse)
    .then(user => {
      if (user.key) {
        localStorage.setItem("user", JSON.stringify(user));
      }
      return user;
    });
}

function logout() {
  localStorage.removeItem("user");
}

function getSpecs() {
  const requestOptions = {
    method: "GET",
    headers: authHeader()
  };
  return fetch(`${config.apiUrl}/specs`, requestOptions).then(handleResponse);
}

function publish(data) {
  let user = JSON.parse(localStorage.getItem("user"));
  const requestOptions = {
    method: "POST",
    headers: {
      "Access-Control-Allow-Methods": "GET, PUT, POST, DELETE, OPTIONS",
      "Content-Type": "application/json",
      Authorization: "Token " + user.key
    },
    body: JSON.stringify(data)
  };
  return fetch(`${config.apiUrl}/publish/`, requestOptions).then(
    handleResponse
  );
}

function handleResponse(response) {
  return response.text().then(text => {
    const data = text && JSON.parse(text);
    if (!response.ok) {
      if (response.status === 401 || response.status === 400) {
        logout();
      }

      const error = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }
    return data;
  });
}

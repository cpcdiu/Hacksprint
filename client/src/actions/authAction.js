import axios from "axios";
import { useHistory } from "react-router-dom";

import {
	USER_LOADING,
	USER_LOADED,
	AUTH_ERROR,
	LOGIN_SUCCESS,
	LOGIN_FAILED,
	SIGNUPSTATE,
} from "./types";

export function loadUser() {
	return function (dispatch, getState) {
		dispatch({ type: USER_LOADING });

		const token = getState().authReducer.token;
		const config = {
			headers: {
				"Content-Type": "application/json",
			},
		};

		if (token) {
			config.headers["Authorization"] = `Token ${token}`;
		}

		axios
			.get(`${process.env.REACT_APP_WEBSITE_NAME}api/user/`, config)
			.then((res) => {
				dispatch({
					type: USER_LOADED,
					payload: res.data,
				});
			})
			.catch((err) => {
				console.log(err);
				dispatch({ type: AUTH_ERROR });
			});
	};
}

export const handleLogin = (user) => (dispatch) => {
	axios
		.post(`${process.env.REACT_APP_WEBSITE_NAME}api/login/`, {
			username: user.username,
			password: user.password,
		})
		.then((res) => {
			const token = res.data.token;
			let user = {
				first_name: res.data.first_name,
				last_name: res.data.last_name,
				email: res.data.email,
				username: res.data.username,
			};
			dispatch({
				type: LOGIN_SUCCESS,
				payload: {
					user: user,
					isAuthenticated: true,
					token: token,
				},
			});
		})
		.catch((err) => {
			console.log(err, "log in error");
			dispatch({
				type: LOGIN_FAILED,
			});
		});
};

export function handleRegister(newUser) {
	return function (dispatch) {
		console.log("register function called");
		axios
			.post(`${process.env.REACT_APP_WEBSITE_NAME}api/register/`, {
				first_name: newUser.first_name,
				last_name: newUser.last_name,
				username: newUser.username,
				email: newUser.email,
				password: newUser.password,
			})
			.then((res) => {
				console.log(res.data);
				dispatch({
					type: SIGNUPSTATE,
					payload: res.data.msg,
				});
			})
			.catch((err) => console.log(err));
	};
}

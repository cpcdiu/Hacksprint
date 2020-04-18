import React, { Component } from "react";

export default class Navbar extends Component {
	render() {
		return (
			<div class="ui large secondary inverted pointing menu m-menu">
				<a class="toc item">
					<i class="sidebar icon"></i>
				</a>
				<a class="active item">Home</a>
				<a class="item">Showcase</a>
				<a class="item">Blog</a>
				<div class="right item">
					<a class="ui inverted button" href="{% url 'login' %}">
						Log in
					</a>
					<a class="ui inverted button" href="{% url 'register' %}">
						Sign Up
					</a>
				</div>
			</div>
		);
	}
}

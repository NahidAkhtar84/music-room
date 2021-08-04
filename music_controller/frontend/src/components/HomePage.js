import React, { Component } from "react";
import JoinRoom from "./JoinRoomPage";
import CreateRoom from "./CreateRoomPage";
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom"

export default class Home extends Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <Router>
                <Switch>
                    <Route exact path="/"><p>This is home page!</p></Route>
                    <Route path="/join" component={JoinRoom}></Route>
                    <Route path="/create" component={CreateRoom}></Route>
                </Switch>
            </Router>
        );
    }
}
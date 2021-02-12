/*
organization inspired by :
https://www.youtube.com/watch?v=tOK9l5uP06U&t=1764s&ab_channel=BriceAyres
*/

import './App.css';
import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import {NavigationBar} from './components/NavigationBar';
import {Home} from './Home';
import {Login} from './Login';
import {CSC} from './CSC';
import {Error} from './Error';
import { CoursePage } from './Course';

function App() {
  return (
    <React.Fragment>
      <NavigationBar />
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/csc" component={CSC} />
          <Route exact path="/course/:courseName" component={CoursePage} />
          <Route component={Error} />
        </Switch>
      </Router> 
    </React.Fragment>
  );
}

export default App;

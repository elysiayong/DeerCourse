/*
organization inspired by :
https://www.youtube.com/watch?v=tOK9l5uP06U&t=1764s&ab_channel=BriceAyres
*/

import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { NavigationBar } from './components/NavigationBar';
import { Home } from './Home';
import { Login } from './Login';
import { CSC } from './CSC';
import { Error } from './Error';
import { CoursePage } from './Course';
import bg from './assets/bg-image2.jpg'
import styled from 'styled-components';

/* style from https://www.youtube.com/watch?v=f8Up35TVNgo&feature=share&ab_channel=JoeBenjamin
 * 
 * Background wraps the contents of each page
 * Background is not used as a flexbox/container
 * in order to not mess with the navbar
 */
const Background = styled.div`
  background-image: url(${bg});
  background-position: left;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  min-height: 100vh;
`

/*
 * Flexbox container for all pages
 */
const Content = styled.div`
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100%;
  width: 100%;
`

function App() {
  return (
    <React.Fragment>
      <Background>
        <NavigationBar />
        <Content>
          <Router>
            <Switch>
              <Route exact path="/" component={Home} />
              <Route exact path="/login" component={Login} />
              <Route exact path="/csc" component={CSC} />
              <Route exact path="/course/:courseName" component={CoursePage} />
              <Route component={Error} />
            </Switch>
          </Router>
        </Content>
      </Background>
    </React.Fragment>
  );
}

export default App;

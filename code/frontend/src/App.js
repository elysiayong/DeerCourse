/*
organization inspired by :
https://www.youtube.com/watch?v=tOK9l5uP06U&t=1764s&ab_channel=BriceAyres
*/

import "./App.css";
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { NavigationBar } from "./components/NavigationBar";
import { Home } from "./Home";
import { Login } from "./Login";
import { CSC } from "./CSC";
import { Programs } from "./Programs";
import { Bookmarks } from "./Bookmarks";
import { Error } from "./Error";
import { CoursePage } from "./CoursePage";
import { Background } from "./components/StyledComponents";
import { SearchResults } from "./SearchResults";

function App() {
  return (
    <React.Fragment>
      <Background>
        <NavigationBar />
        <Router>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/login" component={Login} />
            <Route exact path="/csc" component={CSC} />
            <Route exact path="/programs" component={Programs} />
            <Route exact path="/bookmarks" component={Bookmarks} />
            <Route exact path="/course/:courseName" component={CoursePage} />
            <Route
              exact
              path="/search"
              render={(props) => {
                return (
                  <SearchResults
                    {...props.location.state}
                  />
                );
              }}
            />
            <Route component={Error} />
          </Switch>
        </Router>
      </Background>
    </React.Fragment>
  );
}

export default App;

import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import all from './components/all';
// import search from './components/search';
// import load from './components/load';

class App extends Component {
  render() {
    return (
      <Router>
        <div className="container">
          <nav className="navbar navbar-expand-lg navbar-light" style={{backgroundColor: '#d80011'}}>
            <Link to="/" className="navbar-brand">Home</Link>
            <div className="collpase nav-collapse">
              <ul className="navbar-nav mr-auto">
                <li className="navbar-item">
                  <Link to="/api" className="nav-link">All</Link>
                </li>
                {/* <li className="navbar-item">
                  <Link to="/api/:keyword" className="nav-link">Search By Keyword</Link>
                </li> */}
              </ul>
            </div>
          </nav>
          <Route path="/api" exact component={all} />
          {/* <Route path="/:keyword" component={search} />
          <Route path="/import" component={load} /> */}
        </div>
      </Router>
    );
  }
}

export default App;
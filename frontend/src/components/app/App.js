import React from "react";
import { BrowserRouter as Router,
  Route,
  Switch } from "react-router-dom";
import './App.css';
// components
import Navbar from "../navbar/Navbar";
import Home from "../home/Home";
import VicMap from "../vicmap/VicMap";
import Footer from "../footer/Footer";
import Contact from "../contact/Contact";
import Suburb from "../suburb/Suburb";
import AllSuburbs from "../allsuburbs/AllSuburbs";
import Credits from "../credits/Credits";

const App = () => (
  <Router key={'v0.2'}>
    <div>
      <Navbar />

      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/contact" component={Contact} />
        <Route exact path="/map" component={VicMap} />
        <Route exact path="/suburb" component={AllSuburbs} />
        <Route exact path="/suburb/:name" component={Suburb} />
        <Route exact path="/credits" component={Credits} />
        <Route exact path="/404" component={FourOhFour} />
        <Route component={NoMatch} />
      </Switch>
      <Footer />
    </div>
  </Router>
);

const NoMatch = ({ location }) => (
  <div>
    <main role="main">
        <div className="container">
          <h1>Sorry :(</h1>
          <pre>No match for <code>{location.pathname}</code></pre>
        </div>
    </main>
  </div>
);

const FourOhFour = ({ location }) => (
  <div>
    <main role="main">
        <div className="container">
          <h1>Sorry :(</h1>
          <pre>That page doesn't seem to exist</pre>
        </div>
    </main>
  </div>
);



export default App;
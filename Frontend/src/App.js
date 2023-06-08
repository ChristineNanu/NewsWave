import React, { useEffect } from "react";
import Header from "./components/common/header/Header";
import "./App.css";
import Homepages from "./components/home/Homepages";
import Footer from "./components/common/footer/Footer";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import SinglePage from "./components/singlePage/SinglePage";
import Culture from "./components/culture/Culture";

const App = () => {
  useEffect(() => {
    fetch('http://127.0.0.1:8000/')
      .then(res => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then(data => console.log(data))
      .catch(error => console.log("Fetch error:", error));
  }, []);

  return (
    <>
      <Router>
        <Header />
        <Switch>
          <Route exact path='/' component={Homepages} />
          <Route path='/singlepage/:id' exact component={SinglePage} />
          <Route exact path='/culture' component={Culture} />
        </Switch>
        <Footer />
      </Router>
    </>
  );
};

export default App;

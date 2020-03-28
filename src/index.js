import React from 'react';
import ReactDOM from 'react-dom';
import Rectangle from './Areas/Rectangle';
import SpringConstant from './Areas/SpringConstant'
import { HashRouter, Switch, Route } from "react-router-dom";
import * as serviceWorker from './serviceWorker';

function App() {
  return (
    <div>
      <Switch>
        <Route exact path="/">
          <Rectangle />
        </Route>
        <Route path="/Spring">
          <SpringConstant />
        </Route>
      </Switch>
    </div>
  );
}

ReactDOM.render(
  <HashRouter>
    <App />
  </HashRouter>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

import React from 'react'
import {Container} from 'react-bootstrap'
import Navigation from './components/Navigation'
import './sandstone.css'
import './App.css'
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Stats from './displays/Stats.js'
import MapPage from './displays/MapPage.js'
import ReportPage from './displays/ReportPage'

function App() {
  return (
    <div className="App">
      <Container>
        <h1 className="text-center">Missing Person App</h1>
        <Navigation/>
        <Router>
          <Switch>

            <Route exact path="/" component={MapPage}/>
            <Route path="/report" component={ReportPage}/>
            <Route path="/stats" component={Stats}/>

          </Switch>
        </Router>
        </Container>
    </div>
  );
}

export default App;

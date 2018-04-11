import React from 'react';
import { BrowserRouter, Route, Link, Switch } from 'react-router-dom'
import Nav from './Nav';
import MultipleChoice from './MultipleChoice';
import CreateMultipleChoice from './CreateMultipleChoice';
import Home from './Home';

var Router = BrowserRouter;

class App extends React.Component {
    render () {
        return (
            <Router>
                <div className='container'>
                    <Nav />
                    <Switch>
                        <Route exact path='/' component={Home} />
                        <Route exact path='/answer_question' component={MultipleChoice} />
                        <Route exact path='/create_question' component={CreateMultipleChoice} />
                        <Route render={() => { return <p>N'hi ha res aqui!</p> }} />
                    </Switch>
                </div>
            </Router>
        )
    }
}

module.exports = App;
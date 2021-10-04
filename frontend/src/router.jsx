import React from "react";
import {BrowserRouter, Switch, Route} from "react-router-dom";

import Todolist from './pages/todolist'

const Routes = () => {
    return(
        <BrowserRouter>
            <Switch>
                <Route path='/' component={Todolist} />
            </Switch>
        </BrowserRouter>
    )
}

export default Routes;
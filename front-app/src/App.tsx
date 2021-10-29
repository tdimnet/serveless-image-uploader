import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom"

import HomePage from './pages/Home'
import FilesListPage from './pages/FilesList'
import UploadPage from './pages/Upload'

const App = () => (
    <Router>
        <Switch>
            <Route path='/files-list'>
                <FilesListPage />
            </Route>
            <Route path='/upload'>
                <UploadPage />
            </Route>
            <Route path='/'>
                <HomePage />
            </Route>
        </Switch>
    </Router>
)

export default App

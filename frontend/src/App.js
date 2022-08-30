import React, { Component } from 'react';
import CandidatesTable from './components/CandidatesTable';
import RegistrationForm from './components/RegistrationForm';
import Login from './components/Login';
import axios from 'axios';


export class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      candidatesList: [],
      isAdmin: false
    }
  }

  getRegisteredCandidates = () => {
    const headers = {
      "X-ADMIN": "1"
    }
    axios.get("http://127.0.0.1:8000/api/v1/list-candidates", { headers }).then(res => {
      this.setState({
        candidatesList: res.data
      })
    })
  }

  adminLogin = () => {
    this.setState({ isAdmin: true })
  }

  componentDidUpdate = () => {
    if (this.state.isAdmin) {
      this.getRegisteredCandidates();
    }

  }

  render() {
    return (
      <>
        <div className='container'>
          {this.state.isAdmin ?
            <div className='row mt-4'>
              <CandidatesTable candidatesList={this.state.candidatesList} />
            </div> : <>
              <div className='row mt-4'>
                <RegistrationForm />
              </div>
              <div className='row mt-4'>
                <Login adminLogin={this.adminLogin} />
              </div>
            </>
          }

        </div>
      </>
    )
  }
}

export default App
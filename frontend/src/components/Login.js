import React from 'react'
import Button from 'react-bootstrap/Button';

function Login(props) {
  return (
    <Button variant="primary" onClick={()=>props.adminLogin()}>Login as admin</Button>
  )
}

export default Login
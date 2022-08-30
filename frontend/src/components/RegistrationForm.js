import React from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios';

const RegistrationForm = () => {

  const getFormDataHandler = (e)=>{
    const formData = new FormData();
    const resume = e.target.resume.files[0]
    formData.append("file", resume)
    e.preventDefault();
    const candidateData = {
      full_name:e.target.fullName.value,
      years_of_experience:e.target.yearOfExperience.value,
      date_of_birth:e.target.dateOfBirth.value,
      resume:formData.get("file"),
      department:e.target.position.value
    };
    const headers= {
      'content-type': 'multipart/form-data'
  }
    axios.post("http://127.0.0.1:8000/api/v1/register-candidate/" ,candidateData, {headers}  )
    .then(res=>console.log(res));
    
  }

  return (
    
    <Form onSubmit={(e)=>getFormDataHandler(e)} encType="multipart/form-data">
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Full name</Form.Label>
        <Form.Control type="text" name="fullName" placeholder="Full name" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Years of experience</Form.Label>
        <Form.Control type="number" name="yearOfExperience" placeholder="Years of experience" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Date of birth</Form.Label>
        <Form.Control type="date" name="dateOfBirth" />
      </Form.Group>
      <Form.Group controlId="formFile" className="mb-3">
        <Form.Label>Resume</Form.Label>
        <Form.Control type="file" name="resume" />
      </Form.Group>
      <Form.Group>
        <Form.Select aria-label="Default select example" name="position">
          <option>Select department</option>
          <option value="1">IT</option>
          <option value="2">HR</option>
          <option value="3">Finance</option>
        </Form.Select>
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
    

  )
}

export default RegistrationForm
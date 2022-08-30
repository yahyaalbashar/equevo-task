import React from 'react';
import Button from 'react-bootstrap/Button';
import axios from 'axios';

const DownloadButton= (props)=>{
    const headers={
        "X-ADMIN":"1"
      }
    const downloadResume= (id)=>{
        axios.get(`http://127.0.0.1:8000/api/v1/candidate-resume/${id}`, {headers}).then(res=>{
            window.location.href = res.data.file
        });
    }
  return (
  <Button onClick={()=>downloadResume(props.id)}>download</Button>
)
}

export default DownloadButton
import Table from 'react-bootstrap/Table';
import DownloadButton from './DownloadButton';


const CandidatesTable = (props)=> {
  return (

    <Table striped bordered hover>
      <thead>
        <tr>
          <th>#</th>
          <th>Candidate name</th>
          <th>Date of birth</th>
          <th>Years of experience</th>
          <th>Department</th>
          <th>Resume</th>
        </tr>
      </thead>
      <tbody>
        {
          props.candidatesList.map((item) => {
            return(
            <tr>
              <th>{item.id}</th>
              <th>{item.full_name}</th>
              <th>{item.date_of_birth}</th>
              <th>{item.years_of_experience}</th>
              <th>{item.department}</th>
              <th><DownloadButton id={item.id} headers={props.headers}/></th>
            </tr>
            )         
          })
        }

      </tbody>
    </Table>
  );
}

export default CandidatesTable;
import SearchResults from '../components/SearchResults/SearchResults';
import classes from './SearchView.module.css';
import Modal from '../components/FlatModal/FlatModal';
import { useState } from 'react';

const results = [
  {
    id: 1,
    title: 'Mieszkanie 1',
    price: 100000,
    pricePerMeter: 5000,
    area: 50,
    rooms: 2,
    city: 'Warszawa',
    district: 'Bemowo',
    street: 'Jana Pawła II',
    title: 'Mieszkanie 54m2, zadbane, umeblowane, centrum',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet velit, vitae aliquam nisl nunc eget nunc. Nulla facilisi. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet velit, vitae aliquam nisl nunc eget nunc.',
    images: [
      'https://via.placeholder.com/150',
      'https://via.placeholder.com/150',
      'https://via.placeholder.com/150',
      'https://via.placeholder.com/150',
    ]
  },
  {
    id: 2,
    title: 'Mieszkanie 2',
    price: 100000,
    pricePerMeter: 5000,
    area: 50,
    rooms: 2,
    city: 'Warszawa',
    district: 'Bemowo',
    street: 'Jana Pawła II',
    title: 'Mieszkanie 54m2, zadbane, umeblowane, centrum',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet velit, vitae aliquam nisl nunc eget nunc. Nulla facilisi. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet velit, vitae aliquam nisl nunc eget nunc.',
    images: [
      'https://via.placeholder.com/150',
      'https://via.placeholder.com/150',
      'https://via.placeholder.com/150',
      'https://via.placeholder.com/150',
    ]
  },
]

const SearchView = () => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchResults = (data) => {
    setLoading(true);
    setResults([]);
    setError(null);


    fetch('http://127.0.0.1:8000/flats?'+ new URLSearchParams(data))
    .then(response => {
      if(!response.ok) {
        throw new Error('Something went wrong!');
      }
      return response.json()
    })
    .then(data => {
      setResults(data.message);
      setLoading(false);
    })
    .catch(error => {
      setError(error.message);
      setLoading(false);
    })
  }


  return (
    <>
      <div className={classes.wrapper}>
        <form>
          <input type="text" placeholder="Szukaj" className={classes.searchBar} />
        </form>

        <div className={classes.results}>
          <SearchResults results={results} />
        </div>
      </div>
    </>
  )
}

export default SearchView;
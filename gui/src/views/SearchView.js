import SearchResults from '../components/SearchResults/SearchResults';
import classes from './SearchView.module.css';
import Modal from '../components/FlatModal/FlatModal';
import { useEffect, useState } from 'react';
import HashLoader from "react-spinners/HashLoader";
import searchIcon from '../assets/img/search_icon.svg';

const override = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  display: "block",
  margin: "0 auto",
  borderColor: "red",
};

const SearchView = () => {
  const testResults = [
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

  const [results, setResults] = useState([]);
  const [filteredResults, setFilteredResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searchInputValue, setSearchInputValue] = useState('Warszawa');

  useEffect(() => {
    fetchResults(searchInputValue);
  }, []);

  // debounce auto search after 2 seconds of no typing
  // useEffect(() => {
  //   const identifier = setTimeout(() => {
  //     fetchResults(searchInputValue);
  //   }, 2000);

  //   return () => {
  //     clearTimeout(identifier);
  //   }
  // }, [searchInputValue]);

  const fetchResults = (searchValue) => {
    console.log('fetching results fired');
    setLoading(true);
    setResults([]);
    setFilteredResults([]);
    setError(null);


    fetch('http://127.0.0.1:8069/get_offers2?' + new URLSearchParams({city: searchValue}))
    .then(response => {
      if(!response.ok) {
        throw new Error('Something went wrong!');
      }
      return response.json()
    })
    .then(data => {
      console.log(data);
      setResults(data.offers);
      setLoading(false);

      const filteredResults = data.offers.filter((result) => {
        return result.city.includes(searchInputValue);
      });

      setFilteredResults(filteredResults);
    })
    .catch(error => {
      setError(error.message);
      setLoading(false);
    })
  }

  const searchInputChangeHandler = (event) => {
    const inputValue = event.target.value;
    setSearchInputValue(inputValue);
  }

  const searchHandler = (event) => {
    event.preventDefault();
    fetchResults(searchInputValue);
  }


  return (
    <>
      <div className={classes.wrapper}>
        <form className={classes.searchForm} onSubmit={searchHandler}>
          <input
            type="text"
            placeholder="Szukaj"
            className={classes.searchBar}
            onChange={searchInputChangeHandler}
            value={searchInputValue}
          />
          <button className={classes.submitButton}><img src={searchIcon} /></button>
        </form>

        <div className={classes.results}>
          {filteredResults && <SearchResults results={filteredResults} />}
          {error && <p className={classes.error}>{error}</p>}
        </div>
      </div>
      <HashLoader
        color={'#00FFEF'}
        loading={loading}
        cssOverride={override}
        size={90}
        aria-label="Loading Spinner"
        data-testid="loader"
      />
    </>
  )
}

export default SearchView;
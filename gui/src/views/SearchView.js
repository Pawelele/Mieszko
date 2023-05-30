import SearchResults from '../components/SearchResults/SearchResults';
import classes from './SearchView.module.css';

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
  return (
    <div className={classes.wrapper}>
      <form>
        <input type="text" placeholder="Szukaj" className={classes.searchBar} />
      </form>

      <div className={classes.results}>

        <SearchResults results={results} />

      </div>
    </div>
  )
}

export default SearchView;
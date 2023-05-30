import SearchResult from '../SearchResult/SearchResult';
import classes from './SearchResults.module.css';

const SearchResults = ({ results }) => {
  return (
    <div className={classes.wrapper}>
      {results.map((result) => (
        <div className={classes.result}>
          <SearchResult searchResult={result} />
        </div>
      ))}
    </div>
  )
}

export default SearchResults;
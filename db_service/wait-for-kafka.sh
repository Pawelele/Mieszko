set -e

host="$1"
shift
port="$1"
shift
cmd="$@"

until nc -z "$host" "$port"; do
  >&2 echo "Kafka is unavailable - sleeping"
  sleep 10
done

>&2 echo "Kafka is up - executing command"
exec $cmd
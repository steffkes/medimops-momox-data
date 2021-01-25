#!/bin/bash

ts=$(date -u +"%F_%H-%M-%S")

debug()
{
  echo "`date -u +'%FT%T.%NZ'` $1"
}

ensureDirExists()
{
  dir=`dirname $1`
  [ -d $dir ] || mkdir -p $dir
}

fetchMomox() {

  debug "momox: ($1)"

  path="data/momox/$1/$ts.json"
  ensureDirExists $path

  curl \
    -s \
    -H 'X-API-TOKEN: 2231443b8fb511c7b6a0eb25a62577320bac69b6' \
    -H 'X-MARKETPLACE-ID: momox_de' \
    -H 'Content-Type: application/json' \
    "https://api.momox.de/api/v4/offer/?ean=$1" | \
    python -m json.tool > $path

  sleep 1

  debug "medimops: ($1)"

  path="data/medimops/$1/$ts.jsonl"
  ensureDirExists $path

  echo "$1" | docker-compose run app mix run test.exs > $path

  sleep 1

}

fetchMomox '9783527507993'
fetchMomox '9783593398532'
fetchMomox '9783958751750'
fetchMomox '9781101886724'
fetchMomox '9783734104091'
fetchMomox '9783947188857'
fetchMomox '9783446414396'
fetchMomox '9783548289199'
fetchMomox '9783548289212'
fetchMomox '9783548289229'
fetchMomox '9781101886694'
fetchMomox '9781101904220'
fetchMomox '9783548060224'
fetchMomox '9781409168744'
fetchMomox '9781409168799'

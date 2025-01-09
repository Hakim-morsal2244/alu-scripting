#!/usr/bin/env ruby

regex = /Repetition Token #0/
puts ARGV[0].match(regex) ? "Match" : "No match"

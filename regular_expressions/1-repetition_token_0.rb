#!/usr/bin/env ruby

regex = /hbtt+n/
puts ARGV[0].match(regex) ? "" : ARGV[0]

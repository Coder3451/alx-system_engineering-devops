#!/usr/bin/env ruby
# This ruby script outputs [SENDER],[RECEIVER],[FLAGS].

puts ARGV[0].scan(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/).join(',')

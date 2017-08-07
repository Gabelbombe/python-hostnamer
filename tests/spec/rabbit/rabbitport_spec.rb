# Boilerplate required by ServerSpec
require 'spec_helper'

# And now a test!
describe port(8080) do
  it { should be_listening }
end

describe command('/vagrant/receive_once.py -s localhost') do
  its(:stdout) { should match /rabbit/ }
end
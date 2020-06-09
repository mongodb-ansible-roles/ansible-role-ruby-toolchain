import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ruby_toolchain(host):
    revision = "a650fe6064a65922754444f3fe04c248cdf50ef1"
    assert host.file("/opt/ruby").exists
    assert host.file("/opt/ruby/toolchain_version").exists
    assert host.file("/opt/ruby/toolchain_version").contains(revision)


def test_toolchain_version(host):
    revision = "a650fe6064a65922754444f3fe04c248cdf50ef1"
    assert host.file("/opt/ruby/toolchain_version").exists
    assert host.file("/opt/ruby/toolchain_version").contains(revision)


def test_rubies_symlink(host):
    assert host.file("/root/.rubies").is_symlink
    assert host.file("/root/.rubies").linked_to == "/opt/ruby"

#!/usr/bin/env python3

import sys
import json
import re

lines = []
if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        lines = f.readlines()


def valid_byr(byr):
    try:
        yr = int(byr)
        if yr >= 1920 and yr <= 2002:
            return True
    except:
        pass
    return False


def valid_iyr(iyr):
    try:
        yr = int(iyr)
        if yr >= 2010 and yr <= 2020:
            return True

    except:
        pass
    
    return False


def valid_eyr(eyr):
    try:
        yr = int(eyr)
        if yr >= 2020 and yr <= 2030:
            return True
    except:
        pass
    return False


def valid_hgt(hgt):
    m = re.search("^(\d+)(\w+)$", hgt)
    if m is None:
        return False
    try:
        h = int(m.group(1))
        if m.group(2) == "cm":
            if h >= 150 and h <= 193:
                return True
        if m.group(2) == "in":
            if h >= 59 and h <= 76:
                return True
    except:
        pass
    return False


def valid_hcl(hcl):
    return re.search("^#[0-9a-f]{6}$", hcl) is not None


valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def valid_ecl(ecl):
    return ecl in valid_ecls


def valid_pid(pid):
    return re.search("^\d{9}$", pid) is not None


required_fields = {
    "byr": valid_byr,
    "iyr": valid_iyr,
    "eyr": valid_eyr,
    "hgt": valid_hgt,
    "hcl": valid_hcl,
    "ecl": valid_ecl,
    "pid": valid_pid
}


def new_passport():
    p = {}
    for field in required_fields.keys():
        p[field] = None
    p["cid"] = None
    return p


def valid_passport(passport):
    for field in required_fields.keys():
        if passport[field] is None:
            print("missing field:", field)
            return False

        if not required_fields[field](passport[field]):
            print("invalid", field, passport[field])
            return False

    return True
    

valid_passports = []
cur_passport = new_passport()

for line in lines:
    if len(line.strip()) == 0:
        if valid_passport(cur_passport):
            valid_passports.append(cur_passport)
        cur_passport = new_passport()
        continue

    for field_pair in line.split():
        parts = field_pair.split(":")
        cur_passport[parts[0]] = parts[1].strip()

if valid_passport(cur_passport):
    valid_passports.append(cur_passport)

print(len(valid_passports))


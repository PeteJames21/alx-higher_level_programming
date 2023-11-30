#!/bin/bash
# Add an extra header to the request
curl -sH "X-School-User-Id: 98" "$1"

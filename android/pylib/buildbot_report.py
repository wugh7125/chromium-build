# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Helper functions to print buildbot messages."""

def PrintLink(label, url):
  """Adds a link with name |label| linking to |url| to current buildbot step.

  Args:
    label: A string with the name of the label.
    url: A string of the URL.
  """
  print '@@@STEP_LINK@%s@%s@@@' % (label, url)


def PrintMsg(msg):
  """Appends |msg| to the current buildbot step text.

  Args:
    msg: String to be appended.
  """
  print '@@@STEP_TEXT@%s@@@' % msg


def PrintError():
  """Marks the current step as failed."""
  print '@@@STEP_FAILURE@@@'

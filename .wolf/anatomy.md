# anatomy.md

> Auto-maintained by OpenWolf. Last scanned: 2026-07-09T21:05:33.544Z
> Files: 509 tracked | Anatomy hits: 0 | Misses: 0

## ./

- `.agent-config.toml` (~14 tok)
- `.DS_Store` (~1639 tok)
- `.gitignore` — Git ignore rules (~15 tok)
- `action.yml` (~184 tok)
- `chart.py` — main, str2bool (~666 tok)
- `CLAUDE.md` — OpenWolf (~66 tok)
- `Dockerfile` — Docker container definition (~217 tok)
- `GEMINI.md` (~9 tok)
- `README.md` — Project documentation (~788 tok)

## .claude/

- `settings.json` (~441 tok)

## .claude/rules/

- `openwolf.md` (~313 tok)

## .github/workflows/

- `dev-to-trunk.yml` — CI: Dev to Trunk Auto-PR (~983 tok)
- `pr-to-prod.yml` — CI: 'pypi chart' (~191 tok)

## venv/

- `.DS_Store` (~1639 tok)
- `.gitignore` — Git ignore rules (~19 tok)
- `pyvenv.cfg` (~91 tok)

## venv/bin/

- `activate` — This file must be used with "source bin/activate" *from bash* (~573 tok)
- `activate.csh` — This file must be used with "source bin/activate.csh" *from csh*. (~255 tok)
- `activate.fish` — This file must be used with "source <venv>/bin/activate.fish" *from fish* (~596 tok)
- `Activate.ps1` — Declares from (~2409 tok)
- `chardetect` — -*- coding: utf-8 -*- (~77 tok)
- `f2py` — -*- coding: utf-8 -*- (~76 tok)
- `fonttools` — -*- coding: utf-8 -*- (~76 tok)
- `httpx` — -*- coding: utf-8 -*- (~72 tok)
- `numpy-config` — -*- coding: utf-8 -*- (~76 tok)
- `pip` — -*- coding: utf-8 -*- (~77 tok)
- `pip3` — -*- coding: utf-8 -*- (~77 tok)
- `pip3.13` — -*- coding: utf-8 -*- (~77 tok)
- `pyftmerge` — -*- coding: utf-8 -*- (~75 tok)
- `pyftsubset` — -*- coding: utf-8 -*- (~75 tok)
- `pypistats` — -*- coding: utf-8 -*- (~75 tok)
- `slugify` — -*- coding: utf-8 -*- (~75 tok)
- `ttx` — -*- coding: utf-8 -*- (~75 tok)

## venv/lib/

- `.DS_Store` (~1640 tok)

## venv/lib/python3.13/

- `.DS_Store` (~1640 tok)

## venv/lib/python3.13/site-packages/

- `.DS_Store` (~1640 tok)
- `distutils-precedence.pth` (~41 tok)
- `pylab.py` (~32 tok)
- `six.py` — Utilities for writing code that runs on Python 2 and 3 (~9872 tok)

## venv/lib/python3.13/site-packages/DataProperty-1.0.1.dist-info/

- `INSTALLER` (~2 tok)
- `LICENSE` — Project license (~290 tok)
- `METADATA` (~3065 tok)
- `RECORD` (~900 tok)
- `top_level.txt` (~4 tok)
- `WHEEL` (~25 tok)

## venv/lib/python3.13/site-packages/_distutils_hack/

- `__init__.py` — don't import any costly modules (~1930 tok)
- `override.py` (~13 tok)

## venv/lib/python3.13/site-packages/anyio-4.6.2.post1.dist-info/

- `entry_points.txt` (~10 tok)
- `INSTALLER` (~2 tok)
- `LICENSE` — Project license (~288 tok)
- `METADATA` (~1252 tok)
- `RECORD` (~1486 tok)
- `top_level.txt` (~2 tok)
- `WHEEL` (~25 tok)

## venv/lib/python3.13/site-packages/anyio/

- `__init__.py` — Declares as (~1233 tok)
- `from_thread.py` — _BlockingAsyncContextManager: run, run_sync, run_async_cm, started + 11 more (~4994 tok)
- `lowlevel.py` — View: get, get, get (~1192 tok)
- `py.typed` (~0 tok)
- `pytest_plugin.py` — extract_backend_and_options, get_runner, pytest_configure, pytest_fixture_setup + 7 more (~1918 tok)
- `to_process.py` — from: run_sync, send_raw_command, current_default_process_limiter, process_worker (~2735 tok)
- `to_thread.py` — run_sync, current_default_thread_limiter (~685 tok)

## venv/lib/python3.13/site-packages/anyio/_backends/

- `__init__.py` (~0 tok)
- `_asyncio.py` — from: close, get_loop, run, find_root_task + 2 more (~26142 tok)
- `_trio.py` — from: cancel, deadline, deadline, cancel_called + 25 more (~11518 tok)

## venv/lib/python3.13/site-packages/anyio/_core/

- `__init__.py` (~0 tok)
- `_eventloop.py` — threadlocals: run, sleep, sleep_forever, sleep_until + 5 more (~1341 tok)
- `_exceptions.py` — BrokenResourceError: iterate_exceptions (~709 tok)
- `_fileio.py` — from: wrapped, aclose, read, read1 + 39 more (~5989 tok)
- `_resources.py` — aclose_forcefully (~125 tok)
- `_signals.py` — open_signal_receiver (~259 tok)
- `_sockets.py` — URL configuration (~6940 tok)
- `_streams.py` — Declares create_memory_object_stream (~516 tok)
- `_subprocesses.py` — run_process, drain_stream, open_process (~2218 tok)
- `_synchronization.py` — from: set, is_set, wait, statistics + 28 more (~5749 tok)
- `_tasks.py` — _IgnoredTaskStatus: started, cancel, deadline, deadline + 8 more (~1362 tok)
- `_testing.py` — TaskInfo: has_pending_cancellation, get_current_task, get_running_tasks, wait_all_tasks_blocked (~606 tok)
- `_typedattr.py` — TypedAttributeSet: typed_attribute, extra_attributes, extra, extra + 1 more (~717 tok)

## venv/lib/python3.13/site-packages/anyio/abc/

- `__init__.py` (~766 tok)
- `_eventloop.py` — AsyncBackend: run, current_token, current_time, cancelled_exception_class + 36 more (~2749 tok)
- `_resources.py` — AsyncResource: aclose (~224 tok)
- `_sockets.py` — _NullAsyncContextManager: extra_attributes, send_fds, receive_fds, accept + 3 more (~1790 tok)
- `_streams.py` — UnreliableObjectReceiveStream: receive, send, send_eof, receive + 3 more (~1886 tok)
- `_subprocesses.py` — Process: wait, terminate, kill, send_signal + 5 more (~591 tok)
- `_tasks.py` — TaskStatus: started, started, started, start_soon + 1 more (~781 tok)
- `_testing.py` — TestRunner: run_asyncgen_fixture, run_fixture, run_test (~521 tok)

## venv/lib/python3.13/site-packages/anyio/streams/

- `__init__.py` (~0 tok)
- `buffered.py` — BufferedByteReceiveStream: aclose, buffer, extra_attributes, receive + 2 more (~1286 tok)
- `file.py` — URL configuration (~1253 tok)
- `memory.py` — MemoryObjectStreamStatistics: statistics, receive_nowait, receive, clone + 9 more (~3015 tok)
- `stapled.py` — from: receive, send, send_eof, aclose + 9 more (~1230 tok)
- `text.py` — TextReceiveStream: receive, aclose, extra_attributes, send + 7 more (~1456 tok)
- `tls.py` — from: wrap, unwrap, aclose, receive + 6 more (~3641 tok)

## venv/lib/python3.13/site-packages/certifi-2024.8.30.dist-info/

- `INSTALLER` (~2 tok)
- `LICENSE` — Project license (~264 tok)
- `METADATA` (~593 tok)
- `RECORD` (~271 tok)
- `top_level.txt` (~2 tok)
- `WHEEL` (~25 tok)

## venv/lib/python3.13/site-packages/certifi/

- `__init__.py` (~27 tok)
- `__main__.py` (~70 tok)
- `cacert.pem` — Issuer: CN=GlobalSign Root CA O=GlobalSign nv-sa OU=Root CA (~79848 tok)
- `core.py` — URL patterns: 3 routes (~1265 tok)
- `py.typed` (~0 tok)

## venv/lib/python3.13/site-packages/chardet-5.2.0.dist-info/

- `entry_points.txt` (~15 tok)
- `INSTALLER` (~2 tok)
- `LICENSE` — Project license (~7075 tok)
- `METADATA` (~912 tok)
- `RECORD` (~1942 tok)
- `top_level.txt` (~2 tok)
- `WHEEL` (~25 tok)

## venv/lib/python3.13/site-packages/chardet/

- `__init__.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1371 tok)
- `__main__.py` — Wrapper so people can run python -m chardet (~36 tok)
- `big5freq.py` — ####################### BEGIN LICENSE BLOCK ######################## (~8936 tok)
- `big5prober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~504 tok)
- `chardistribution.py` — ####################### BEGIN LICENSE BLOCK ######################## (~2867 tok)
- `charsetgroupprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1119 tok)
- `charsetprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1549 tok)
- `codingstatemachine.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1067 tok)
- `codingstatemachinedict.py` — Declares CodingStateMachineDict (~155 tok)
- `cp949prober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~532 tok)
- `enums.py` — InputState: get_num_categories (~481 tok)
- `escprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1145 tok)
- `escsm.py` — ####################### BEGIN LICENSE BLOCK ######################## (~3479 tok)
- `eucjpprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1124 tok)
- `euckrfreq.py` — ####################### BEGIN LICENSE BLOCK ######################## (~3876 tok)
- `euckrprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~501 tok)
- `euctwfreq.py` — ####################### BEGIN LICENSE BLOCK ######################## (~10547 tok)
- `euctwprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~501 tok)
- `gb2312freq.py` — ####################### BEGIN LICENSE BLOCK ######################## (~5925 tok)
- `gb2312prober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~503 tok)
- `hebrewprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~4154 tok)
- `jisfreq.py` — ####################### BEGIN LICENSE BLOCK ######################## (~7371 tok)
- `johabfreq.py` — ####################### BEGIN LICENSE BLOCK ######################## (~12143 tok)
- `johabprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~501 tok)
- `jpcntx.py` — ####################### BEGIN LICENSE BLOCK ######################## (~7730 tok)
- `langbulgarianmodel.py` — 3: Positive (~28636 tok)
- `langgreekmodel.py` — 3: Positive (~27008 tok)
- `langhebrewmodel.py` — 3: Positive (~26986 tok)
- `langhungarianmodel.py` — 3: Positive (~28589 tok)
- `langrussianmodel.py` — 3: Positive (~35055 tok)
- `langthaimodel.py` — 3: Positive (~26958 tok)
- `langturkishmodel.py` — 3: Positive (~26958 tok)
- `latin1prober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1538 tok)
- `macromanprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1737 tok)
- `mbcharsetprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1062 tok)
- `mbcsgroupprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~609 tok)
- `mbcssm.py` — ####################### BEGIN LICENSE BLOCK ######################## (~8684 tok)
- `py.typed` (~0 tok)
- `resultdict.py` — Declares ResultDict (~115 tok)
- `sbcharsetprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1829 tok)
- `sbcsgroupprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1182 tok)
- `sjisprober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~1145 tok)
- `universaldetector.py` — ####################### BEGIN LICENSE BLOCK ######################## (~4243 tok)
- `utf1632prober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~2430 tok)
- `utf8prober.py` — ####################### BEGIN LICENSE BLOCK ######################## (~804 tok)
- `version.py` (~70 tok)

## venv/lib/python3.13/site-packages/chardet/cli/

- `__init__.py` (~0 tok)
- `chardetect.py` — description_of, main (~927 tok)

## venv/lib/python3.13/site-packages/chardet/metadata/

- `__init__.py` (~0 tok)
- `languages.py` — Declares Language (~3563 tok)

## venv/lib/python3.13/site-packages/contourpy-1.3.1.dist-info/

- `INSTALLER` (~2 tok)
- `LICENSE` — Project license (~410 tok)
- `METADATA` (~1447 tok)
- `RECORD` (~783 tok)
- `WHEEL` (~25 tok)

## venv/lib/python3.13/site-packages/contourpy/

- `__init__.py` — name: contour_generator (~3381 tok)
- `_contourpy.pyi` — Input numpy array types, the same as in common.h (~1900 tok)
- `_version.py` (~7 tok)
- `array.py` — codes_from_offsets, codes_from_offsets_and_points, codes_from_points, concat_codes + 16 more (~2566 tok)
- `chunk.py` — calc_chunk_sizes, two_factors (~937 tok)
- `convert.py` — convert_filled (~7473 tok)
- `dechunk.py` — dechunk_filled, dechunk_lines, dechunk_multi_filled, dechunk_multi_lines (~2216 tok)
- `enum_util.py` — as_fill_type, as_line_type, as_z_interp (~434 tok)
- `py.typed` (~0 tok)
- `typecheck.py` — check_code_array, check_offset_array, check_point_array, check_filled + 1 more (~3071 tok)
- `types.py` — dtypes of arrays returned by ContourPy. (~71 tok)

## venv/lib/python3.13/site-packages/contourpy/util/

- `__init__.py` (~34 tok)
- `_build_config.py` — _build_config.py.in is converted into _build_config.py during the meson build process. (~570 tok)
- `bokeh_renderer.py` — BokehRenderer: filled, grid, lines, mask + 5 more (~3934 tok)
- `bokeh_util.py` — filled_to_bokeh, lines_to_bokeh (~802 tok)
- `data.py` — simple, random (~739 tok)
- `mpl_renderer.py` — MplRenderer: filled, grid, lines, mask + 5 more (~5740 tok)
- `mpl_util.py` — filled_to_mpl_paths, lines_to_mpl_paths (~987 tok)
- `renderer.py` — Renderer: filled, grid, lines, mask + 7 more (~1463 tok)

## venv/lib/python3.13/site-packages/cycler-0.12.1.dist-info/

- `INSTALLER` (~2 tok)
- `LICENSE` — Project license (~400 tok)
- `METADATA` (~1008 tok)
- `RECORD` (~180 tok)
- `top_level.txt` (~2 tok)
- `WHEEL` (~25 tok)

## venv/lib/python3.13/site-packages/cycler/

- `__init__.py` — Cycler: concat, keys, change_key, by_key (~4774 tok)
- `py.typed` (~0 tok)

## venv/lib/python3.13/site-packages/dataproperty/

- `__init__.py` — Declares import (~374 tok)
- `__version__.py` (~58 tok)
- `_align_getter.py` — AlignGetter: typecode_align_table, typecode_align_table, get_align_from_typecode (~238 tok)
- `_align.py` — Align: align_code, align_string (~153 tok)
- `_base.py` — DataPeropertyBase: type_class, typecode, typename, format_str (~719 tok)
- `_column.py` — ColumnDataProperty: align, bit_length, column_index, decimal_places + 13 more (~3330 tok)
- `_common.py` — DefaultValue: default_datetime_formatter (~548 tok)
- `_container.py` — AbstractContainer: min_value, max_value, mean, update + 16 more (~1466 tok)
- `_converter.py` — DataPropertyConverter: convert (~934 tok)
- `_dataproperty.py` — DataProperty: align, decimal_places, data, is_include_ansi_escape + 7 more (~3235 tok)
- `_extractor.py` — MatrixFormatting: headers, headers, default_type_hint, default_type_hint + 38 more (~7400 tok)
- `_formatter.py` — Format: make_format_map, make_format_str (~858 tok)
- `_function.py` — DigitCalculator: get_integer_digit, get_decimal_places, get_number_of_digit, strip_ansi_escape + 1 more (~890 tok)
- `_interface.py` — DataPeropertyInterface: align, decimal_places, typecode, typename (~179 tok)
- `_line_break.py` — Declares import (~33 tok)
- `_preprocessor.py` — Preprocessor: normalize_lbh, line_break_handling, line_break_handling, preprocess + 1 more (~1562 tok)
- `py.typed` (~0 tok)
- `typing.py` — normalize_type_hint (~401 tok)

## venv/lib/python3.13/site-packages/dataproperty/logger/

- `__init__.py` (~26 tok)
- `_logger.py` — set_logger (~127 tok)
- `_null_logger.py` — NullLogger: remove, add, disable, enable + 9 more (~306 tok)

## venv/lib/python3.13/site-packages/dateutil/

- `__init__.py` — -*- coding: utf-8 -*- (~178 tok)
- `_common.py` — Declares weekday (~267 tok)
- `_version.py` — file generated by setuptools_scm (~48 tok)
- `easter.py` — -*- coding: utf-8 -*- (~766 tok)
- `relativedelta.py` — -*- coding: utf-8 -*- (~7116 tok)
- `rrule.py` — -*- coding: utf-8 -*- (~19017 tok)
- `tzwin.py` — tzwin has moved to dateutil.tz.win (~17 tok)
- `utils.py` — -*- coding: utf-8 -*- (~562 tok)

## venv/lib/python3.13/site-packages/dateutil/parser/

- `__init__.py` — -*- coding: utf-8 -*- (~505 tok)
- `_parser.py` — -*- coding: utf-8 -*- (~16799 tok)
- `isoparser.py` — -*- coding: utf-8 -*- (~3780 tok)

## venv/lib/python3.13/site-packages/dateutil/tz/

- `__init__.py` — -*- coding: utf-8 -*- (~127 tok)
- `_common.py` — of: tzname_in_python2, adjust_encoding, enfold, replace + 10 more (~3708 tok)
- `_factories.py` — _TzSingleton: instance (~734 tok)
- `tz.py` — -*- coding: utf-8 -*- (~17959 tok)
- `win.py` — -*- coding: utf-8 -*- (~3696 tok)

## venv/lib/python3.13/site-packages/dateutil/zoneinfo/

- `__init__.py` — -*- coding: utf-8 -*- (~1683 tok)
- `rebuild.py` — rebuild (~684 tok)

## venv/lib/python3.13/site-packages/dominate-2.9.1.dist-info/

- `INSTALLER` (~2 tok)
- `LICENSE.txt` — Declares provided (~1910 tok)
- `METADATA` — Declares for (~3647 tok)
- `RECORD` (~394 tok)
- `top_level.txt` (~3 tok)
- `WHEEL` (~30 tok)

## venv/lib/python3.13/site-packages/dominate/

- `__init__.py` (~26 tok)
- `_version.py` (~7 tok)
- `document.py` — document: get_title, set_title, add (~641 tok)
- `dom_tag.py` — View: get (~4038 tok)
- `dom1core.py` — dom1core: parentNode, getElementById, getElementsByTagName, appendChild (~496 tok)
- `svg.py` — URL configuration (~2606 tok)
- `tags.py` — html_tag: validate, validate_attributes, validate_context, validate_content + 3 more (~8184 tok)
- `util.py` — container: include, system, escape, unescape + 3 more (~1232 tok)

## venv/lib/python3.13/site-packages/fontTools/

- `__init__.py` (~53 tok)
- `__main__.py` — main (~265 tok)
- `afmLib.py` — Module for reading and writing AFM (Adobe Font Metrics) files. (~3762 tok)
- `agl.py` — -*- coding: utf-8 -*- (~32161 tok)
- `fontBuilder.py` — is: drawTestGlyph, drawTestGlyph, usBreakChar, save + 4 more (~9701 tok)
- `help.py` — main (~322 tok)
- `tfmLib.py` — Module for reading TFM (TeX Font Metrics) files. (~4074 tok)
- `ttx.py` — Options: ttList, ttDump, ttCompile (~4758 tok)
- `unicode.py` — _UnicodeCustom: setUnicodeData (~354 tok)

## venv/lib/python3.13/site-packages/fontTools/cffLib/

- `__init__.py` — cffLib: read/write Adobe CFF fonts (~30596 tok)
- `CFF2ToCFF.py` — CFF2 to CFF converter. (~1740 tok)
- `CFFToCFF2.py` — CFF to CFF2 converter. (~2892 tok)
- `specializer.py` — T2CharString operator specializer and generalizer. (~9298 tok)
- `transforms.py` — StopHintCountEvent: execute, op_callsubr, op_callgsubr, stop_hint_count + 18 more (~4901 tok)
- `width.py` — T2CharString glyph width optimizer. (~1736 tok)

## venv/lib/python3.13/site-packages/fontTools/colorLib/

- `__init__.py` (~0 tok)
- `builder.py` — ColorPaletteType: populateCOLRv0, buildCOLR, buildClipList, buildClipBox + 2 more (~6574 tok)
- `errors.py` — Declares ColorLibError (~12 tok)
- `geometry.py` — Helpers for manipulating 2D points and vectors in COLR table. (~1576 tok)
- `table_builder.py` — BuildCallback: build, unbuild (~2134 tok)
- `unbuilder.py` — LayerListUnbuilder: unbuildColrV1, unbuildPaint (~612 tok)

## venv/lib/python3.13/site-packages/fontTools/config/

- `__init__.py` — Declares can (~755 tok)

## venv/lib/python3.13/site-packages/fontTools/cu2qu/

- `__init__.py` — you may not use this file except in compliance with the License. (~177 tok)
- `__main__.py` (~27 tok)
- `benchmark.py` — Benchmark the cu2qu algorithm performance. (~371 tok)
- `cli.py` — URL configuration (~1736 tok)
- `cu2qu.c` (~169561 tok)
- `cu2qu.py` — cython: language_level=3 (~4705 tok)
- `errors.py` — you may not use this file except in compliance with the License. (~698 tok)
- `ufo.py` — Converts cubic bezier curves to quadratic splines. (~3370 tok)

## venv/lib/python3.13/site-packages/fontTools/designspaceLib/

- `__init__.py` — DesignSpaceDocumentError: posix, posixpath_property, getter, setter + 8 more (~36920 tok)
- `__main__.py` (~30 tok)
- `split.py` — Allows building all the variable fonts of a DesignSpace version 5 by (~5497 tok)
- `statNames.py` — Compute name information for a given location in user-space coordinates (~2592 tok)
- `types.py` — from: clamp, intersection, locationInRegion, regionInRegion + 2 more (~1520 tok)

## venv/lib/python3.13/site-packages/fontTools/encodings/

- `__init__.py` — Empty __init__.py file to signal Python this directory is a package. (~22 tok)
- `codecs.py` — Extend the Python codecs module with a few encodings that are used in OpenType (name table) (~1349 tok)
- `MacRoman.py` (~1022 tok)
- `StandardEncoding.py` (~1024 tok)

## venv/lib/python3.13/site-packages/fontTools/feaLib/

- `__init__.py` — fontTools.feaLib -- a package for dealing with OpenType feature files. (~61 tok)
- `__main__.py` — main (~640 tok)
- `ast.py` — Element: deviceToString, asFea, build, asFea + 23 more (~21086 tok)
- `builder.py` — Builder: addOpenTypeFeatures, addOpenTypeFeaturesFromString, build, elif + 4 more (~19999 tok)
- `error.py` — Declares FeatureLibError (~184 tok)
- `lexer.c` (~214502 tok)
- `lexer.py` — Lexer: next, location_, next_, scan_over_ + 5 more (~3178 tok)
- `location.py` — Declares FeatureLibLocation (~67 tok)
- `lookupDebugInfo.py` — Declares LookupDebugInfo (~87 tok)
- `parser.py` — Parser: parse, parse_anchor_, is, parse_anchor_marks_ + 6 more (~28134 tok)
- `variableScalar.py` — VariableScalar: Location, does_vary, axes_dict, fix_location + 7 more (~1163 tok)

## venv/lib/python3.13/site-packages/fontTools/merge/

- `__init__.py` — Google Author(s): Behdad Esfahbod, Roozbeh Pournader (~2358 tok)
- `__main__.py` (~27 tok)
- `base.py` — Google Author(s): Behdad Esfahbod, Roozbeh Pournader (~683 tok)
- `cmap.py` — Google Author(s): Behdad Esfahbod, Roozbeh Pournader (~1585 tok)
- `layout.py` — Google Author(s): Behdad Esfahbod, Roozbeh Pournader (~4593 tok)
- `options.py` — Google Author(s): Behdad Esfahbod, Roozbeh Pournader (~715 tok)
- `tables.py` — Google Author(s): Behdad Esfahbod, Roozbeh Pournader (~3040 tok)
- `unicode.py` — is_Default_Ignorable (~1221 tok)
- `util.py` — Google Author(s): Behdad Esfahbod, Roozbeh Pournader (~966 tok)

## venv/lib/python3.13/site-packages/fontTools/misc/

- `__init__.py` — Empty __init__.py file to signal Python this directory is a package. (~22 tok)
- `arrayTools.py` — Routines for calculating bounding boxes, point in rectangle calculations and (~3281 tok)
- `bezierTools.py` — fontTools.misc.bezierTools.py -- tools for working with Bezier path segments. (~12787 tok)
- `classifyTools.py` — fontTools.misc.classifyTools.py -- tools for classifying things. (~1604 tok)
- `cliTools.py` — Collection of utilities for command-line interfaces and console scripts. (~532 tok)
- `configTools.py` — of: parse_optional_bool, validate_optional_bool, register, register_option + 6 more (~3197 tok)
- `cython.py` — Exports a no-op 'cython' namespace similar to (~195 tok)
- `dictTools.py` — Misc dict tools. (~691 tok)
- `eexec.py` — decrypt, encrypt, hexString, deHexString (~952 tok)
- `encodingTools.py` — fontTools.misc.encodingTools.py -- tools for working with OpenType encodings. (~593 tok)
- `etree.py` — Shim module exporting the same ElementTree API for lxml and (~4880 tok)
- `filenames.py` — NameTranslationError: userNameToFileName, handleClash1, handleClash2 (~2350 tok)
- `fixedTools.py` — fixedToFloat, floatToFixed, floatToFixedToFloat, fixedToStr + 5 more (~2185 tok)
- `intTools.py` — bit_count, bit_indices (~168 tok)
- `iterTools.py` — Python 3.12: (~112 tok)
- `lazyTools.py` — Declares LazyDict (~292 tok)
- `loggingTools.py` — default logging level used by Timer class (~5686 tok)
- `macCreatorType.py` — getMacCreatorAndType, setMacCreatorAndType (~456 tok)
- `macRes.py` — ResourceError: openResourceFork, openDataFork, keys, types + 7 more (~2452 tok)
- `psCharStrings.py` — psCharStrings.py -- module implementing various kinds of CharStrings: (~12296 tok)
- `psLib.py` — PSTokenError: read, close, getnexttoken, skipwhite + 20 more (~3457 tok)
- `psOperators.py` — ps_object: put, ps_def, ps_bind, proc_bind + 34 more (~4486 tok)
- `py23.py` — Python 2/3 compat layer leftovers. (~640 tok)
- `roundTools.py` — noRound, otRound, maybeRound, roundFunc + 1 more (~907 tok)
- `sstruct.py` — sstruct.py -- SuperStruct (~2046 tok)
- `symfont.py` — _BezierFuncsLazy: green, printGreenPen (~2004 tok)
- `testTools.py` — Helpers for writing unit tests. (~1981 tok)
- `textTools.py` — fontTools.misc.textTools.py -- miscellaneous routines. (~965 tok)
- `timeTools.py` — fontTools.misc.timeTools.py -- tools for working with OpenType timestamps. (~639 tok)
- `transform.py` — Affine 2D transformation matrix class. (~4235 tok)
- `treeTools.py` — Generic tools for working with trees. (~363 tok)
- `vector.py` — Vector: length, normalized, dot, toInt + 3 more (~1161 tok)
- `visitor.py` — Generic visitor pattern implementation for Python objects. (~1519 tok)
- `xmlReader.py` — TTXParseError: read, close, set, increment + 1 more (~1880 tok)
- `xmlWriter.py` — xmlWriter.py -- Simple XML authoring class (~1728 tok)

## venv/lib/python3.13/site-packages/fontTools/misc/plistlib/

- `__init__.py` — Data: fromBase64, asBase64, start, end + 16 more (~6033 tok)
- `py.typed` (~0 tok)

## venv/lib/python3.13/site-packages/fontTools/mtiLib/

- `__init__.py` — FontDame-to-FontTools for OpenType Layout tables (~13320 tok)
- `__main__.py` (~27 tok)

## venv/lib/python3.13/site-packages/fontTools/otlLib/

- `__init__.py` — OpenType Layout-related functionality. (~13 tok)
- `builder.py` — LookupBuilder: buildCoverage, buildLookup, equals, inferGlyphClasses + 20 more (~34198 tok)
- `error.py` — Declares OpenTypeLibError (~96 tok)
- `maxContextCalc.py` — maxCtxFont, maxCtxSubtable, maxCtxContextualSubtable, maxCtxContextualRule (~908 tok)

## venv/lib/python3.13/site-packages/fontTools/otlLib/optimize/

- `__init__.py` — main (~438 tok)
- `__main__.py` (~30 tok)
- `gpos.py` — kerning: compact, compact_lookup, compact_ext_lookup, compact_pair_pos + 8 more (~5273 tok)

## venv/lib/python3.13/site-packages/fontTools/pens/

- `__init__.py` — Empty __init__.py file to signal Python this directory is a package. (~22 tok)
- `areaPen.py` — Calculate the area of a glyph. (~421 tok)
- `basePen.py` — fontTools.pens.basePen.py -- Tools and base classes to build pen objects. (~4878 tok)
- `boundsPen.py` — ControlBoundsPen: init (~894 tok)
- `cairoPen.py` — Pen to draw to a Cairo graphics library context. (~170 tok)
- `cocoaPen.py` — Declares CocoaPen (~175 tok)
- `cu2quPen.py` — you may not use this file except in compliance with the License. (~3717 tok)
- `explicitClosingLinePen.py` — ExplicitClosingLinePen: filterContour (~920 tok)
- `filterPen.py` — _PassThruComponentsMixin: addComponent, moveTo, lineTo, curveTo + 10 more (~2226 tok)
- `freetypePen.py` — Pen to rasterize paths with FreeType. (~5679 tok)
- `hashPointPen.py` — Modified from https://github.com/adobe-type-tools/psautohint/blob/08b346865710ed3c172f1eb581d6ef243b203f99/python/psautohint/ufoFont.py#L800-L838 (~1021 tok)
- `momentsPen.c` (~154588 tok)
- `momentsPen.py` — Declares MomentsPen (~7339 tok)
- `perimeterPen.py` — Calculate the perimeter of a glyph. (~616 tok)
- `pointInsidePen.py` — fontTools.pens.pointInsidePen -- Pen implementing "point inside" testing (~1816 tok)
- `pointPen.py` — AbstractPointPen: beginPath, endPath, addPoint, addComponent + 12 more (~6371 tok)
- `qtPen.py` — URL configuration (~182 tok)
- `qu2cuPen.py` — you may not use this file except in compliance with the License. (~1139 tok)
- `quartzPen.py` — URL configuration (~368 tok)
- `recordingPen.py` — Pen recording operations that can be accessed or replayed. (~3569 tok)
- `reportLabPen.py` — Declares ReportLabPen (~591 tok)
- `reverseContourPen.py` — ReverseContourPen: filterContour, reversedContour (~1150 tok)
- `roundingPen.py` — RoundingPen: moveTo, lineTo, curveTo, qCurveTo + 3 more (~1329 tok)
- `statisticsPen.py` — Pen calculating area, center of mass, variance and standard-deviation, (~2755 tok)
- `svgPathPen.py` — SVGPathPen: pointToString, getCommands, main (~2450 tok)
- `t2CharStringPen.py` — Author: Tal Leming (~684 tok)
- `teePen.py` — Pen multiplexing drawing to one or more pens. (~369 tok)
- `transformPen.py` — TransformPen: moveTo, lineTo, curveTo, qCurveTo + 5 more (~1159 tok)
- `ttGlyphPen.py` — _TTGlyphBasePen: init, addComponent, glyph, lineTo + 9 more (~3392 tok)
- `wxPen.py` — URL configuration (~195 tok)

## venv/lib/python3.13/site-packages/fontTools/qu2cu/

- `__init__.py` — you may not use this file except in compliance with the License. (~177 tok)
- `__main__.py` (~27 tok)
- `benchmark.py` — Benchmark the qu2cu algorithm performance. (~400 tok)
- `cli.py` (~1062 tok)
- `qu2cu.c` (~188244 tok)
- `qu2cu.py` — cython: language_level=3 (~3519 tok)

## venv/lib/python3.13/site-packages/fontTools/subset/

- `__init__.py` — Google Author(s): Behdad Esfahbod (~38259 tok)
- `__main__.py` (~28 tok)
- `cff.py` — _ClosureGlyphsT2Decompiler: op_endchar, closure_glyphs, prune_pre_subset, subset_glyphs + 4 more (~1756 tok)
- `svg.py` — URL patterns: 3 routes (~2682 tok)
- `util.py` — Private utility methods used by the subset modules (~216 tok)

## venv/lib/python3.13/site-packages/fontTools/svgLib/

- `__init__.py` (~22 tok)

## venv/lib/python3.13/site-packages/fontTools/svgLib/path/

- `__init__.py` — URL configuration (~571 tok)
- `arc.py` — Convert SVG Path's elliptical arcs to Bezier curves. (~1661 tok)
- `parser.py` — SVG Path specification parser. (~3083 tok)
- `shapes.py` — URL patterns: 2 routes (~1521 tok)

## venv/lib/python3.13/site-packages/fontTools/t1Lib/

- `__init__.py` — fontTools.t1Lib.py -- Tools for PostScript Type 1 fonts. (~5962 tok)

## venv/lib/python3.13/site-packages/fontTools/ttLib/

- `__init__.py` — fontTools.ttLib -- a package for dealing with TrueType fonts. (~158 tok)
- `__main__.py` — main (~984 tok)
- `macUtils.py` — ttLib.macUtils.py -- Various Mac-specific stuff. (~497 tok)
- `removeOverlaps.py` — Simplify TrueType glyphs by merging overlapping contours/components. (~3604 tok)
- `reorderGlyphs.py` — Reorder glyphs in a font. (~2948 tok)
- `scaleUpem.py` — Change the units-per-EM of a font. (~4177 tok)
- `sfnt.py` — ttLib/sfnt.py -- low-level module to deal with the sfnt file format. (~6524 tok)
- `standardGlyphOrder.py` — 'post' table formats 1.0 and 2.0 rely on this list of "standard" (~1653 tok)
- `ttCollection.py` — TTCollection: close, save, saveXML (~1133 tok)
- `ttFont.py` — TTFont: close, save, saveXML (~11708 tok)
- `ttGlyphSet.py` — GlyphSets returned by a TTFont. (~4965 tok)
- `ttVisitor.py` — Specialization of fontTools.misc.visitor to work with TTFont. (~293 tok)
- `woff2.py` — WOFF2Reader: reconstructTable, close (~17446 tok)

## venv/lib/python3.13/site-packages/fontTools/ttLib/tables/

- `__init__.py` — DON'T EDIT! This file is generated by MetaTools/buildTableList.py. (~750 tok)
- `_a_n_k_r.py` — Declares table__a_n_k_r (~132 tok)
- `_a_v_a_r.py` — table__a_v_a_r: compile, decompile, toXML, fromXML + 1 more (~2011 tok)
- `_b_s_l_n.py` — https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6bsln.html (~49 tok)
- `_c_i_d_g.py` — coding: utf-8 (~224 tok)
- `_c_m_a_p.py` — table__c_m_a_p: getcmap, getBestCmap, buildReversed, decompile + 9 more (~17613 tok)
- `_c_v_a_r.py` — table__c_v_a_r: compile, decompile, fromXML, toXML (~945 tok)
- `_c_v_t.py` — table__c_v_t: decompile, compile, toXML, fromXML (~389 tok)
- `_f_e_a_t.py` — Declares table__f_e_a_t (~160 tok)
- `_f_p_g_m.py` — table__f_p_g_m: decompile, compile, toXML, fromXML (~335 tok)
- `_f_v_a_r.py` — table__f_v_a_r: compile, decompile, toXML, fromXML + 9 more (~2455 tok)
- `_g_a_s_p.py` — table__g_a_s_p: decompile, compile, toXML, fromXML (~548 tok)
- `_g_c_i_d.py` — https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6gcid.html (~49 tok)
- `_g_l_y_f.py` — _g_l_y_f.py -- Converter classes for the 'glyf' table. (~24152 tok)
- `_g_v_a_r.py` — table__g_v_a_r: compile, compileGlyphs_, decompile, get_read_item + 9 more (~2976 tok)
- `_h_d_m_x.py` — _GlyphnamedList: keys, decompile, compile, toXML + 1 more (~1150 tok)
- `_h_e_a_d.py` — table__h_e_a_d: decompile, compile, toXML, fromXML (~1356 tok)
- `_h_h_e_a.py` — table__h_h_e_a: ascender, ascender, descender, descender + 5 more (~1267 tok)
- `_h_m_t_x.py` — table__h_m_t_x: decompile, compile, toXML, fromXML (~1648 tok)
- `_k_e_r_n.py` — table__k_e_r_n: getkern, decompile, compile, toXML + 9 more (~2982 tok)
- `_l_c_a_r.py` — Declares table__l_c_a_r (~26 tok)
- `_l_o_c_a.py` — table__l_o_c_a: decompile, compile, set, toXML (~548 tok)
- `_l_t_a_g.py` — https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6ltag.html (~650 tok)
- `_m_a_x_p.py` — table__m_a_x_p: decompile, compile, recalc, testrepr + 2 more (~1446 tok)
- `_m_e_t_a.py` — Apple's documentation of 'meta': (~1044 tok)
- `_m_o_r_t.py` — https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6mort.html (~49 tok)
- `_m_o_r_x.py` — https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6morx.html (~49 tok)
- `_n_a_m_e.py` — -*- coding: utf-8 -*- (~11639 tok)
- `_o_p_b_d.py` — https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6opbd.html (~49 tok)
- `_p_o_s_t.py` — table__p_o_s_t: decompile, compile, getGlyphOrder, decode_format_1_0 + 10 more (~3224 tok)
- `_p_r_e_p.py` — Declares table__p_r_e_p (~33 tok)
- `_p_r_o_p.py` — https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6prop.html (~49 tok)
- `_s_b_i_x.py` — table__s_b_i_x: decompile, compile, toXML, fromXML (~1270 tok)
- `_t_r_a_k.py` — table__t_r_a_k: compile, decompile, toXML, fromXML + 9 more (~3163 tok)
- `_v_h_e_a.py` — table__v_h_e_a: decompile, compile, recalc, toXML + 3 more (~1180 tok)
- `_v_m_t_x.py` — Declares table__v_m_t_x (~66 tok)
- `asciiTable.py` — asciiTable: toXML, fromXML (~182 tok)
- `B_A_S_E_.py` — Declares table_B_A_S_E_ (~26 tok)
- `BitmapGlyphMetrics.py` — Since bitmap glyph metrics are shared between EBLC and EBDT (~506 tok)
- `C_B_D_T_.py` — Google Author(s): Matt Fontaine (~952 tok)
- `C_B_L_C_.py` — Google Author(s): Matt Fontaine (~54 tok)
- `C_F_F__2.py` — table_C_F_F__2: decompile, compile (~122 tok)
- `C_F_F_.py` — table_C_F_F_: decompile, compile, haveGlyphNames, getGlyphOrder + 3 more (~413 tok)
- `C_O_L_R_.py` — Google Author(s): Behdad Esfahbod (~1636 tok)
- `C_P_A_L_.py` — Google Author(s): Behdad Esfahbod (~3324 tok)
- `D__e_b_g.py` — table_D__e_b_g: decompile, compile, toXML, fromXML (~127 tok)
- `D_S_I_G_.py` — table_D_S_I_G_: decompile, compile, toXML, fromXML + 3 more (~1522 tok)
- `DefaultTable.py` — DefaultTable: decompile, compile, toXML, fromXML (~425 tok)
- `E_B_D_T_.py` — table_E_B_D_T_: getImageFormatClass, decompile, compile, toXML + 3 more (~9222 tok)
- `E_B_L_C_.py` — table_E_B_L_C_: getIndexFormatClass, decompile, compile, toXML + 3 more (~8509 tok)
- `F__e_a_t.py` — table_F__e_a_t: decompile, compile, toXML, fromXML (~1538 tok)
- `F_F_T_M_.py` — table_F_F_T_M_: decompile, compile, toXML, fromXML (~387 tok)
- `G__l_a_t.py` — from itertools import * (~2448 tok)
- `G__l_o_c.py` — table_G__l_o_c: decompile, compile, set, toXML + 1 more (~743 tok)
- `G_D_E_F_.py` — Declares table_G_D_E_F_ (~26 tok)
- `G_M_A_P_.py` — GMAPRecord: toXML, fromXML, compile, decompile + 3 more (~1290 tok)
- `G_P_K_G_.py` — table_G_P_K_G_: decompile, compile, toXML, fromXML (~1269 tok)
- `G_P_O_S_.py` — Declares table_G_P_O_S_ (~26 tok)
- `G_S_U_B_.py` — Declares table_G_S_U_B_ (~26 tok)
- `grUtils.py` — decompress, compress, entries, bininfo + 2 more (~649 tok)
- `H_V_A_R_.py` — Declares table_H_V_A_R_ (~26 tok)
- `J_S_T_F_.py` — Declares table_J_S_T_F_ (~26 tok)
- `L_T_S_H_.py` — XXX I've lowered the strictness, to make sure Apple's own Chicago (~522 tok)
- `M_A_T_H_.py` — Declares table_M_A_T_H_ (~26 tok)
- `M_E_T_A_.py` — table_M_E_T_A_: getLabelString, decompile, compile, toXML + 9 more (~3367 tok)
- `M_V_A_R_.py` — Declares table_M_V_A_R_ (~26 tok)
- `O_S_2f_2.py` — Panose: toXML, fromXML, decompile, compile + 13 more (~7916 tok)
- `otBase.py` — OverflowErrorRecord: decompile, compile, tryPackingHarfbuzz, tryPackingFontTools + 20 more (~15245 tok)
- `otConverters.py` — in: buildConverters, readArray, get_read_item, read_item + 47 more (~21164 tok)
- `otData.py` (~56354 tok)
- `otTables.py` — fontTools.ttLib.tables.otTables -- A collection of classes representing the various (~27688 tok)
- `otTraverse.py` — Methods for traversing trees of otData-driven OpenType tables. (~1571 tok)
- `S__i_l_f.py` — from itertools import * (~9972 tok)
- `S__i_l_l.py` — table_S__i_l_l: decompile, compile, toXML, fromXML (~887 tok)
- `S_I_N_G_.py` — table_S_I_N_G_: decompile, decompileUniqueName, compile, compilecompileUniqueName + 2 more (~890 tok)
- `S_T_A_T_.py` — Declares table_S_T_A_T_ (~26 tok)
- `S_V_G_.py` — Compiles/decompiles SVG table. (~2133 tok)
- `sbixGlyph.py` — Glyph: is_reference_type, decompile, compile, toXML + 1 more (~1656 tok)
- `sbixStrike.py` — Strike: decompile, compile, toXML, fromXML (~1904 tok)
- `T_S_I__0.py` — TSI{0,1,2,3,5} are private tables used by Microsoft Visual TrueType (VTT) (~584 tok)
- `T_S_I__1.py` — TSI{0,1,2,3,5} are private tables used by Microsoft Visual TrueType (VTT) (~1995 tok)
- `T_S_I__2.py` — TSI{0,1,2,3,5} are private tables used by Microsoft Visual TrueType (VTT) (~120 tok)
- `T_S_I__3.py` — TSI{0,1,2,3,5} are private tables used by Microsoft Visual TrueType (VTT) (~134 tok)
- `T_S_I__5.py` — TSI{0,1,2,3,5} are private tables used by Microsoft Visual TrueType (VTT) (~432 tok)
- `T_S_I_B_.py` — Declares table_T_S_I_B_ (~25 tok)
- `T_S_I_C_.py` — Declares table_T_S_I_C_ (~26 tok)
- `T_S_I_D_.py` — Declares table_T_S_I_D_ (~25 tok)
- `T_S_I_J_.py` — Declares table_T_S_I_J_ (~25 tok)
- `T_S_I_P_.py` — Declares table_T_S_I_P_ (~25 tok)
- `T_S_I_S_.py` — Declares table_T_S_I_S_ (~25 tok)
- `T_S_I_V_.py` — table_T_S_I_V_: toXML, fromXML (~188 tok)
- `T_T_F_A_.py` — Declares table_T_T_F_A_ (~24 tok)
- `table_API_readme.txt` — Declares table__g_l_y_f (~687 tok)
- `ttProgram.py` — ttLib.tables.ttProgram.py -- Assembler/disassembler for TrueType bytecode programs. (~10254 tok)
- `TupleVariation.py` — TupleVariation: getUsedPoints, hasImpact, toXML, fromXML + 7 more (~9210 tok)
- `V_A_R_C_.py` — Declares table_V_A_R_C_ (~26 tok)
- `V_D_M_X_.py` — table_V_D_M_X_: decompile, compile, toXML, fromXML (~2912 tok)
- `V_O_R_G_.py` — table_V_O_R_G_: decompile, compile, toXML, fromXML + 2 more (~1647 tok)
- `V_V_A_R_.py` — Declares table_V_V_A_R_ (~26 tok)

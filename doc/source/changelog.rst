.. _ref_release_notes:

Release notes
#############

This document contains the release notes for the project.

.. vale off

.. towncrier release notes start

`0.4.0b1 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.4.0b1>`_ - September 04, 2026
=============================================================================================
No significant changes.
`0.4.0 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.4.0>`_ - September 03, 2026
=========================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Add get_target/get_source on connections and fix transactional commit field names
          - `#189 <https://github.com/ansys/pysam-sysml2/pull/189>`_

        * - Add scripting get(name) accessor for non-dot-accessible names
          - `#191 <https://github.com/ansys/pysam-sysml2/pull/191>`_

        * - Surface renamed name/visibility fields through deprecation shims
          - `#192 <https://github.com/ansys/pysam-sysml2/pull/192>`_

        * - Align metamodel
          - `#197 <https://github.com/ansys/pysam-sysml2/pull/197>`_

        * - Add opt-in resolve_libraries flag to load and map library element contents
          - `#207 <https://github.com/ansys/pysam-sysml2/pull/207>`_

        * - Read and write complex value expressions as text
          - `#209 <https://github.com/ansys/pysam-sysml2/pull/209>`_

        * - Resolve feature chaining
          - `#215 <https://github.com/ansys/pysam-sysml2/pull/215>`_

        * - Change valuation reading process
          - `#231 <https://github.com/ansys/pysam-sysml2/pull/231>`_

        * - Support includesDerived/includesInherited and derive local collections
          - `#273 <https://github.com/ansys/pysam-sysml2/pull/273>`_

        * - Forward includes_derived/includes_inherited on execute_query and element resolution
          - `#295 <https://github.com/ansys/pysam-sysml2/pull/295>`_

        * - Add ForwardedNotification class and extend properties in Classifier, Feature, and Type
          - `#302 <https://github.com/ansys/pysam-sysml2/pull/302>`_

        * - Enhance derived collections and testing framework, fix issues with missing reconstruction on derived collections
          - `#304 <https://github.com/ansys/pysam-sysml2/pull/304>`_

        * - Add api version check
          - `#352 <https://github.com/ansys/pysam-sysml2/pull/352>`_


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Rework FeatureValue set-value commits and drop legacy defaultValue paths
          - `#186 <https://github.com/ansys/pysam-sysml2/pull/186>`_

        * - Make IPython autocomplete honor element __dir__ via complete_object hook
          - `#193 <https://github.com/ansys/pysam-sysml2/pull/193>`_

        * - Resolve no-name elements via their ElementType and ID declared name
          - `#212 <https://github.com/ansys/pysam-sysml2/pull/212>`_

        * - Hide private backing fields from static element autocomplete
          - `#214 <https://github.com/ansys/pysam-sysml2/pull/214>`_

        * - Add enum support
          - `#237 <https://github.com/ansys/pysam-sysml2/pull/237>`_

        * - Change name to declared_name in unchanged code
          - `#244 <https://github.com/ansys/pysam-sysml2/pull/244>`_

        * - Preload roots before build and resolve root package via Namespace
          - `#272 <https://github.com/ansys/pysam-sysml2/pull/272>`_

        * - Round-trip LiteralString values with KerML string-literal escaping
          - `#275 <https://github.com/ansys/pysam-sysml2/pull/275>`_

        * - Repair e2e transactional documentation links and KerML literal string updates
          - `#288 <https://github.com/ansys/pysam-sysml2/pull/288>`_

        * - Improve library package retrieval logic in ProjectImpl
          - `#305 <https://github.com/ansys/pysam-sysml2/pull/305>`_

        * - Get libraries package() should not raise error
          - `#354 <https://github.com/ansys/pysam-sysml2/pull/354>`_


  .. tab-item:: Documentation

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Migration guide
          - `#230 <https://github.com/ansys/pysam-sysml2/pull/230>`_

        * - Replace XMI models with KPAR models for bike and computer examples
          - `#311 <https://github.com/ansys/pysam-sysml2/pull/311>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Regenerate static metamodel for the new SysML2 API
          - `#184 <https://github.com/ansys/pysam-sysml2/pull/184>`_

        * - Update CHANGELOG for v0.3.3
          - `#356 <https://github.com/ansys/pysam-sysml2/pull/356>`_


  .. tab-item:: Miscellaneous

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Adapt builder and mappers to the regenerated metamodel
          - `#185 <https://github.com/ansys/pysam-sysml2/pull/185>`_

        * - Use a dot-safe ClassName_<id> fallback for empty-name elements
          - `#187 <https://github.com/ansys/pysam-sysml2/pull/187>`_

        * - Adapt builder to FeatureChaining with lazy inherited-proxy caching
          - `#188 <https://github.com/ansys/pysam-sysml2/pull/188>`_

        * - Remove rest api support for diagrams
          - `#243 <https://github.com/ansys/pysam-sysml2/pull/243>`_

        * - Move parse_and_set_value from elements to SysMLTools
          - `#255 <https://github.com/ansys/pysam-sysml2/pull/255>`_

        * - Expose real UUID for inherited elements instead of self-built composed IDs
          - `#256 <https://github.com/ansys/pysam-sysml2/pull/256>`_

        * - Add SysMLTools.get_element_visibility and remove name and visibility deprecation shims
          - `#257 <https://github.com/ansys/pysam-sysml2/pull/257>`_

        * - Unify metamodel
          - `#269 <https://github.com/ansys/pysam-sysml2/pull/269>`_


  .. tab-item:: Test

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update e2e tests
          - `#271 <https://github.com/ansys/pysam-sysml2/pull/271>`_

        * - Refresh modeltestset fixtures and resolve mock project dirs by UUID
          - `#303 <https://github.com/ansys/pysam-sysml2/pull/303>`_


`0.3.3 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.3.3>`_ - September 02, 2026
=========================================================================================

.. tab-set::


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update ansys action version due to release error
          - `#355 <https://github.com/ansys/pysam-sysml2/pull/355>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump ansys/actions/release-github from 11.0.2 to 11.0.3
          - `#348 <https://github.com/ansys/pysam-sysml2/pull/348>`_

        * - Bump ansys/actions/tests-pytest from 11.0.2 to 11.0.3
          - `#349 <https://github.com/ansys/pysam-sysml2/pull/349>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.3.2
          - `#347 <https://github.com/ansys/pysam-sysml2/pull/347>`_


`0.3.2 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.3.2>`_ - September 01, 2026
=========================================================================================

.. tab-set::


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Prefix kwargs with _ for scripting elements in factory transactional mode
          - `#154 <https://github.com/ansys/pysam-sysml2/pull/154>`_

        * - Separate project manager cache for scripting and SysML project types
          - `#155 <https://github.com/ansys/pysam-sysml2/pull/155>`_

        * - Get_value method fixed for SysMLElement and SysMLInheritedElement …
          - `#346 <https://github.com/ansys/pysam-sysml2/pull/346>`_


  .. tab-item:: Documentation

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Fix example title and add project management guide
          - `#157 <https://github.com/ansys/pysam-sysml2/pull/157>`_

        * - Update \`\`CONTRIBUTORS.md\`\` with the latest contributors
          - `#163 <https://github.com/ansys/pysam-sysml2/pull/163>`_

        * - Update README with MIGRATING section.rst
          - `#228 <https://github.com/ansys/pysam-sysml2/pull/228>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump pytest from 9.0.2 to 9.0.3
          - `#156 <https://github.com/ansys/pysam-sysml2/pull/156>`_

        * - Bump idna from 3.11 to 3.13
          - `#161 <https://github.com/ansys/pysam-sysml2/pull/161>`_

        * - Bump pre-commit from 4.5.1 to 4.6.0
          - `#162 <https://github.com/ansys/pysam-sysml2/pull/162>`_

        * - Bump ansys/actions from 10.2.12 to 10.3.0
          - `#164 <https://github.com/ansys/pysam-sysml2/pull/164>`_

        * - Adopt prek as the local pre-commit replacement
          - `#166 <https://github.com/ansys/pysam-sysml2/pull/166>`_

        * - Bump actions/labeler from 6.0.1 to 6.1.0
          - `#167 <https://github.com/ansys/pysam-sysml2/pull/167>`_

        * - Bump ansys/actions from 10.3.0 to 10.3.1
          - `#176 <https://github.com/ansys/pysam-sysml2/pull/176>`_

        * - Bump pytest-mock from 3.14.0 to 3.15.1
          - `#177 <https://github.com/ansys/pysam-sysml2/pull/177>`_

        * - Bump ansys-sphinx-theme from 1.7.2 to 1.8.1
          - `#178 <https://github.com/ansys/pysam-sysml2/pull/178>`_

        * - Bump ansys/actions from 10.3.1 to 10.3.2
          - `#179 <https://github.com/ansys/pysam-sysml2/pull/179>`_

        * - Bump ansys-sphinx-theme from 1.8.1 to 1.8.2
          - `#182 <https://github.com/ansys/pysam-sysml2/pull/182>`_

        * - Bump actions/checkout from 6.0.2 to 6.0.3
          - `#190 <https://github.com/ansys/pysam-sysml2/pull/190>`_

        * - Bump prek from 0.3.2 to 0.4.4
          - `#198 <https://github.com/ansys/pysam-sysml2/pull/198>`_

        * - Bump prek from 0.4.4 to 0.4.5
          - `#202 <https://github.com/ansys/pysam-sysml2/pull/202>`_

        * - Bump actions/checkout from 6.0.3 to 7.0.0
          - `#203 <https://github.com/ansys/pysam-sysml2/pull/203>`_

        * - Bump ansys-sphinx-theme from 1.8.2 to 1.9.0
          - `#204 <https://github.com/ansys/pysam-sysml2/pull/204>`_

        * - Bump pytest from 9.0.3 to 9.1.1
          - `#205 <https://github.com/ansys/pysam-sysml2/pull/205>`_

        * - Bump ansys/actions/code-style from 10.3.2 to 10.3.3
          - `#217 <https://github.com/ansys/pysam-sysml2/pull/217>`_

        * - Bump ansys/actions/doc-deploy-dev from 10.3.2 to 10.3.3
          - `#218 <https://github.com/ansys/pysam-sysml2/pull/218>`_

        * - Bump ansys/actions/check-actions-security from 10.3.2 to 10.3.3
          - `#219 <https://github.com/ansys/pysam-sysml2/pull/219>`_

        * - Bump ansys/actions/doc-style from 10.3.2 to 10.3.3
          - `#220 <https://github.com/ansys/pysam-sysml2/pull/220>`_

        * - Bump ansys/actions/doc-deploy-changelog from 10.3.2 to 10.3.3
          - `#221 <https://github.com/ansys/pysam-sysml2/pull/221>`_

        * - Bump ansys/actions/build-wheelhouse from 10.3.2 to 10.3.3
          - `#222 <https://github.com/ansys/pysam-sysml2/pull/222>`_

        * - Bump ansys/actions/doc-build from 10.3.2 to 10.3.3
          - `#223 <https://github.com/ansys/pysam-sysml2/pull/223>`_

        * - Bump ansys/actions/release-github from 10.3.2 to 10.3.3
          - `#224 <https://github.com/ansys/pysam-sysml2/pull/224>`_

        * - Bump ansys/actions/doc-deploy-stable from 10.3.2 to 10.3.3
          - `#225 <https://github.com/ansys/pysam-sysml2/pull/225>`_

        * - Bump ansys/actions/build-library from 10.3.2 to 10.3.3
          - `#226 <https://github.com/ansys/pysam-sysml2/pull/226>`_

        * - Bump prek from 0.4.5 to 0.4.8
          - `#229 <https://github.com/ansys/pysam-sysml2/pull/229>`_

        * - Bump ansys/actions/check-vulnerabilities from 10.3.2 to 10.3.3
          - `#232 <https://github.com/ansys/pysam-sysml2/pull/232>`_

        * - Bump actions/labeler from 6.1.0 to 6.2.0
          - `#233 <https://github.com/ansys/pysam-sysml2/pull/233>`_

        * - Bump ansys/actions/tests-pytest from 10.3.2 to 10.3.3
          - `#234 <https://github.com/ansys/pysam-sysml2/pull/234>`_

        * - Bump ansys/actions/check-pr-title from 10.3.2 to 10.3.4
          - `#238 <https://github.com/ansys/pysam-sysml2/pull/238>`_

        * - Bump ansys/actions/check-vulnerabilities from 10.3.3 to 10.3.4
          - `#239 <https://github.com/ansys/pysam-sysml2/pull/239>`_

        * - Bump ansys/actions/check-actions-security from 10.3.3 to 10.3.4
          - `#240 <https://github.com/ansys/pysam-sysml2/pull/240>`_

        * - Bump ansys/actions/doc-deploy-dev from 10.3.3 to 10.3.4
          - `#241 <https://github.com/ansys/pysam-sysml2/pull/241>`_

        * - Bump ansys/actions/doc-changelog from 10.3.2 to 10.3.4
          - `#242 <https://github.com/ansys/pysam-sysml2/pull/242>`_

        * - Bump ansys/actions/doc-deploy-stable from 10.3.3 to 10.3.4
          - `#245 <https://github.com/ansys/pysam-sysml2/pull/245>`_

        * - Bump ansys/actions/code-style from 10.3.3 to 10.3.4
          - `#246 <https://github.com/ansys/pysam-sysml2/pull/246>`_

        * - Bump ansys/actions/tests-pytest from 10.3.3 to 10.3.4
          - `#247 <https://github.com/ansys/pysam-sysml2/pull/247>`_

        * - Bump ansys/actions/build-library from 10.3.3 to 10.3.4
          - `#248 <https://github.com/ansys/pysam-sysml2/pull/248>`_

        * - Bump ansys/actions/doc-deploy-changelog from 10.3.3 to 10.3.4
          - `#249 <https://github.com/ansys/pysam-sysml2/pull/249>`_

        * - Bump ansys/actions/release-github from 10.3.3 to 10.3.4
          - `#250 <https://github.com/ansys/pysam-sysml2/pull/250>`_

        * - Bump ansys/actions/doc-style from 10.3.3 to 10.3.4
          - `#251 <https://github.com/ansys/pysam-sysml2/pull/251>`_

        * - Bump prek from 0.4.8 to 0.4.9
          - `#252 <https://github.com/ansys/pysam-sysml2/pull/252>`_

        * - Bump ansys/actions/build-wheelhouse from 10.3.3 to 10.3.4
          - `#253 <https://github.com/ansys/pysam-sysml2/pull/253>`_

        * - Bump ansys/actions/doc-build from 10.3.3 to 10.3.4
          - `#254 <https://github.com/ansys/pysam-sysml2/pull/254>`_

        * - Bump ansys/actions/check-vulnerabilities from 10.3.4 to 10.3.5
          - `#258 <https://github.com/ansys/pysam-sysml2/pull/258>`_

        * - Bump ansys/actions/tests-pytest from 10.3.4 to 10.3.5
          - `#259 <https://github.com/ansys/pysam-sysml2/pull/259>`_

        * - Bump prek from 0.4.9 to 0.4.10
          - `#260 <https://github.com/ansys/pysam-sysml2/pull/260>`_

        * - Bump ansys/actions/build-library from 10.3.4 to 10.3.5
          - `#261 <https://github.com/ansys/pysam-sysml2/pull/261>`_

        * - Bump actions/labeler from 6.2.0 to 7.0.0
          - `#262 <https://github.com/ansys/pysam-sysml2/pull/262>`_

        * - Bump ansys/actions/doc-deploy-changelog from 10.3.4 to 10.3.5
          - `#263 <https://github.com/ansys/pysam-sysml2/pull/263>`_

        * - Bump ansys/actions/doc-style from 10.3.4 to 10.3.5
          - `#264 <https://github.com/ansys/pysam-sysml2/pull/264>`_

        * - Bump ansys/actions/doc-changelog from 10.3.4 to 10.3.5
          - `#265 <https://github.com/ansys/pysam-sysml2/pull/265>`_

        * - Bump ansys/actions/build-wheelhouse from 10.3.4 to 10.3.5
          - `#266 <https://github.com/ansys/pysam-sysml2/pull/266>`_

        * - Bump ansys/actions/doc-deploy-dev from 10.3.4 to 10.3.5
          - `#267 <https://github.com/ansys/pysam-sysml2/pull/267>`_

        * - Bump ansys/actions/code-style from 10.3.4 to 10.3.5
          - `#268 <https://github.com/ansys/pysam-sysml2/pull/268>`_

        * - Bump prek from 0.4.10 to 0.4.11
          - `#270 <https://github.com/ansys/pysam-sysml2/pull/270>`_

        * - Bump ansys/actions/doc-build from 10.3.4 to 10.3.5
          - `#276 <https://github.com/ansys/pysam-sysml2/pull/276>`_

        * - Bump ansys/actions/doc-deploy-stable from 10.3.4 to 10.3.5
          - `#277 <https://github.com/ansys/pysam-sysml2/pull/277>`_

        * - Bump ansys/actions/release-github from 10.3.4 to 10.3.5
          - `#278 <https://github.com/ansys/pysam-sysml2/pull/278>`_

        * - Bump pypa/gh-action-pypi-publish from 1.14.0 to 1.14.2
          - `#279 <https://github.com/ansys/pysam-sysml2/pull/279>`_

        * - Bump actions/checkout from 7.0.0 to 7.0.1
          - `#280 <https://github.com/ansys/pysam-sysml2/pull/280>`_

        * - Bump ansys/actions/check-pr-title from 10.3.4 to 10.3.5
          - `#281 <https://github.com/ansys/pysam-sysml2/pull/281>`_

        * - Bump ansys/actions/check-actions-security from 10.3.4 to 10.3.5
          - `#282 <https://github.com/ansys/pysam-sysml2/pull/282>`_

        * - Bump ansys/actions/doc-deploy-dev from 10.3.5 to 10.3.6
          - `#283 <https://github.com/ansys/pysam-sysml2/pull/283>`_

        * - Bump ansys/actions/release-github from 10.3.5 to 10.3.6
          - `#284 <https://github.com/ansys/pysam-sysml2/pull/284>`_

        * - Bump ansys/actions/check-pr-title from 10.3.5 to 10.3.6
          - `#285 <https://github.com/ansys/pysam-sysml2/pull/285>`_

        * - Bump ansys/actions/tests-pytest from 10.3.5 to 10.3.6
          - `#286 <https://github.com/ansys/pysam-sysml2/pull/286>`_

        * - Bump ansys/actions/check-vulnerabilities from 10.3.5 to 10.3.6
          - `#287 <https://github.com/ansys/pysam-sysml2/pull/287>`_

        * - Bump ansys/actions/doc-build from 10.3.5 to 10.3.6
          - `#289 <https://github.com/ansys/pysam-sysml2/pull/289>`_

        * - Bump prek from 0.4.11 to 0.4.12
          - `#290 <https://github.com/ansys/pysam-sysml2/pull/290>`_

        * - Bump ansys/actions/doc-deploy-stable from 10.3.5 to 10.3.6
          - `#291 <https://github.com/ansys/pysam-sysml2/pull/291>`_

        * - Bump ansys/actions/code-style from 10.3.5 to 10.3.6
          - `#292 <https://github.com/ansys/pysam-sysml2/pull/292>`_

        * - Bump ansys/actions/doc-style from 10.3.5 to 10.3.6
          - `#293 <https://github.com/ansys/pysam-sysml2/pull/293>`_

        * - Bump ansys/actions/doc-changelog from 10.3.5 to 10.3.6
          - `#294 <https://github.com/ansys/pysam-sysml2/pull/294>`_

        * - Bump ansys/actions/check-actions-security from 10.3.5 to 10.3.6
          - `#296 <https://github.com/ansys/pysam-sysml2/pull/296>`_

        * - Bump ansys/actions/build-wheelhouse from 10.3.5 to 10.3.6
          - `#297 <https://github.com/ansys/pysam-sysml2/pull/297>`_

        * - Bump ansys-sphinx-theme from 1.9.0 to 1.10.0
          - `#298 <https://github.com/ansys/pysam-sysml2/pull/298>`_

        * - Update flit-core requirement from <4,>=3.2 to >=3.2,<5
          - `#299 <https://github.com/ansys/pysam-sysml2/pull/299>`_

        * - Bump ansys/actions/build-library from 10.3.5 to 10.3.6
          - `#300 <https://github.com/ansys/pysam-sysml2/pull/300>`_

        * - Bump ansys/actions/doc-deploy-changelog from 10.3.5 to 10.3.6
          - `#301 <https://github.com/ansys/pysam-sysml2/pull/301>`_

        * - Bump ansys/actions/tests-pytest from 10.3.6 to 11.0.0
          - `#306 <https://github.com/ansys/pysam-sysml2/pull/306>`_

        * - Bump ansys/actions/build-wheelhouse from 10.3.6 to 11.0.0
          - `#307 <https://github.com/ansys/pysam-sysml2/pull/307>`_

        * - Bump ansys/actions/doc-style from 10.3.6 to 11.0.0
          - `#308 <https://github.com/ansys/pysam-sysml2/pull/308>`_

        * - Bump ansys/actions/build-library from 10.3.6 to 11.0.0
          - `#309 <https://github.com/ansys/pysam-sysml2/pull/309>`_

        * - Bump ansys/actions/doc-changelog from 10.3.6 to 11.0.0
          - `#310 <https://github.com/ansys/pysam-sysml2/pull/310>`_

        * - Bump ansys/actions/build-library from 11.0.0 to 11.0.1
          - `#312 <https://github.com/ansys/pysam-sysml2/pull/312>`_

        * - Bump ansys/actions/doc-style from 11.0.0 to 11.0.1
          - `#313 <https://github.com/ansys/pysam-sysml2/pull/313>`_

        * - Bump ansys/actions/release-github from 10.3.6 to 11.0.1
          - `#314 <https://github.com/ansys/pysam-sysml2/pull/314>`_

        * - Bump ansys/actions/build-wheelhouse from 11.0.0 to 11.0.1
          - `#315 <https://github.com/ansys/pysam-sysml2/pull/315>`_

        * - Bump prek from 0.4.12 to 0.4.13
          - `#316 <https://github.com/ansys/pysam-sysml2/pull/316>`_

        * - Bump ansys/actions/doc-deploy-stable from 10.3.6 to 11.0.1
          - `#317 <https://github.com/ansys/pysam-sysml2/pull/317>`_

        * - Bump ansys/actions/check-pr-title from 10.3.6 to 11.0.2
          - `#318 <https://github.com/ansys/pysam-sysml2/pull/318>`_

        * - Bump ansys/actions/tests-pytest from 11.0.0 to 11.0.2
          - `#319 <https://github.com/ansys/pysam-sysml2/pull/319>`_

        * - Bump ansys/actions/doc-deploy-stable from 11.0.1 to 11.0.2
          - `#320 <https://github.com/ansys/pysam-sysml2/pull/320>`_

        * - Bump ansys/actions/check-vulnerabilities from 10.3.6 to 11.0.2
          - `#321 <https://github.com/ansys/pysam-sysml2/pull/321>`_

        * - Bump ansys/actions/check-actions-security from 10.3.6 to 11.0.2
          - `#322 <https://github.com/ansys/pysam-sysml2/pull/322>`_

        * - Bump ansys/actions/build-wheelhouse from 11.0.1 to 11.0.2
          - `#323 <https://github.com/ansys/pysam-sysml2/pull/323>`_

        * - Bump ansys/actions/doc-style from 11.0.1 to 11.0.2
          - `#324 <https://github.com/ansys/pysam-sysml2/pull/324>`_

        * - Bump ansys/actions/doc-deploy-changelog from 10.3.6 to 11.0.2
          - `#325 <https://github.com/ansys/pysam-sysml2/pull/325>`_

        * - Bump ansys/actions/release-github from 11.0.1 to 11.0.2
          - `#326 <https://github.com/ansys/pysam-sysml2/pull/326>`_

        * - Bump ansys/actions/doc-deploy-dev from 10.3.6 to 11.0.2
          - `#327 <https://github.com/ansys/pysam-sysml2/pull/327>`_

        * - Bump ansys/actions/build-library from 11.0.1 to 11.0.2
          - `#331 <https://github.com/ansys/pysam-sysml2/pull/331>`_

        * - Bump ansys/actions/doc-deploy-stable from 11.0.2 to 11.0.3
          - `#332 <https://github.com/ansys/pysam-sysml2/pull/332>`_

        * - Bump ansys/actions/check-actions-security from 11.0.2 to 11.0.3
          - `#333 <https://github.com/ansys/pysam-sysml2/pull/333>`_

        * - Bump ansys/actions/doc-style from 11.0.2 to 11.0.3
          - `#334 <https://github.com/ansys/pysam-sysml2/pull/334>`_

        * - Bump prek from 0.4.13 to 0.4.14
          - `#335 <https://github.com/ansys/pysam-sysml2/pull/335>`_

        * - Bump ansys/actions/build-wheelhouse from 11.0.2 to 11.0.3
          - `#336 <https://github.com/ansys/pysam-sysml2/pull/336>`_

        * - Bump ansys/actions/doc-changelog from 11.0.0 to 11.0.3
          - `#337 <https://github.com/ansys/pysam-sysml2/pull/337>`_

        * - Bump ansys/actions/build-library from 11.0.2 to 11.0.3
          - `#338 <https://github.com/ansys/pysam-sysml2/pull/338>`_

        * - Bump ansys/actions/doc-deploy-changelog from 11.0.2 to 11.0.3
          - `#339 <https://github.com/ansys/pysam-sysml2/pull/339>`_

        * - Bump ansys/actions/code-style from 10.3.6 to 11.0.3
          - `#340 <https://github.com/ansys/pysam-sysml2/pull/340>`_

        * - Bump ansys/actions/doc-deploy-dev from 11.0.2 to 11.0.3
          - `#341 <https://github.com/ansys/pysam-sysml2/pull/341>`_

        * - Bump ansys/actions/doc-build from 10.3.6 to 11.0.3
          - `#342 <https://github.com/ansys/pysam-sysml2/pull/342>`_

        * - Bump ansys/actions/check-vulnerabilities from 11.0.2 to 11.0.3
          - `#343 <https://github.com/ansys/pysam-sysml2/pull/343>`_

        * - Bump ansys/actions/check-pr-title from 11.0.2 to 11.0.3
          - `#344 <https://github.com/ansys/pysam-sysml2/pull/344>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.3.1
          - `#151 <https://github.com/ansys/pysam-sysml2/pull/151>`_

        * - Update missing or outdated files
          - `#160 <https://github.com/ansys/pysam-sysml2/pull/160>`_, `#206 <https://github.com/ansys/pysam-sysml2/pull/206>`_, `#274 <https://github.com/ansys/pysam-sysml2/pull/274>`_

        * - Drop Python 3.10 and 3.11 based on SPEC-0 and internal reqs
          - `#200 <https://github.com/ansys/pysam-sysml2/pull/200>`_


  .. tab-item:: Miscellaneous

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Clean up unnecessary iterations and improve code patterns
          - `#138 <https://github.com/ansys/pysam-sysml2/pull/138>`_


  .. tab-item:: Test

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Refactor test and add e2e test structure
          - `#158 <https://github.com/ansys/pysam-sysml2/pull/158>`_

        * - Force e2e tests to succeed for ado pipeline validation
          - `#194 <https://github.com/ansys/pysam-sysml2/pull/194>`_


`0.3.1 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.3.1>`_ - April 13, 2026
=====================================================================================

.. tab-set::


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Handle empty commits and return None for missing elements #149
          - `#150 <https://github.com/ansys/pysam-sysml2/pull/150>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump requests from 2.33.0 to 2.33.1
          - `#146 <https://github.com/ansys/pysam-sysml2/pull/146>`_

        * - Bump ansys/actions from 10.2.7 to 10.2.12
          - `#147 <https://github.com/ansys/pysam-sysml2/pull/147>`_

        * - Bump werkzeug from 3.1.7 to 3.1.8
          - `#148 <https://github.com/ansys/pysam-sysml2/pull/148>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.3.0
          - `#145 <https://github.com/ansys/pysam-sysml2/pull/145>`_


`0.3.0 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.3.0>`_ - April 09, 2026
=====================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Add create and delete methods to project manager
          - `#139 <https://github.com/ansys/pysam-sysml2/pull/139>`_


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Incorrect super() call in ObservedList.__delitem__ (#135)
          - `#136 <https://github.com/ansys/pysam-sysml2/pull/136>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump pytest-cov from 7.0.0 to 7.1.0
          - `#128 <https://github.com/ansys/pysam-sysml2/pull/128>`_

        * - Bump werkzeug from 3.1.6 to 3.1.7
          - `#133 <https://github.com/ansys/pysam-sysml2/pull/133>`_

        * - Bump requests from 2.32.5 to 2.33.0
          - `#134 <https://github.com/ansys/pysam-sysml2/pull/134>`_

        * - Bump pypa/gh-action-pypi-publish from 1.13.0 to 1.14.0
          - `#140 <https://github.com/ansys/pysam-sysml2/pull/140>`_


  .. tab-item:: Miscellaneous

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Optimize performance across codebase
          - `#141 <https://github.com/ansys/pysam-sysml2/pull/141>`_


  .. tab-item:: Documentation

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Fix typos, syntax issues and clean up documentation (#130)
          - `#132 <https://github.com/ansys/pysam-sysml2/pull/132>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.2.2
          - `#126 <https://github.com/ansys/pysam-sysml2/pull/126>`_


`0.2.2 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.2.2>`_ - March 31, 2026
=====================================================================================

.. tab-set::


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Refactor owner check for SysML element #124
          - `#125 <https://github.com/ansys/pysam-sysml2/pull/125>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump actions/download-artifact from 8.0.0 to 8.0.1
          - `#119 <https://github.com/ansys/pysam-sysml2/pull/119>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.2.1
          - `#122 <https://github.com/ansys/pysam-sysml2/pull/122>`_


`0.2.1 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.2.1>`_ - March 24, 2026
=====================================================================================

.. tab-set::


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Improve attribute assignment condition for inherited elements #120
          - `#121 <https://github.com/ansys/pysam-sysml2/pull/121>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.2.0
          - `#118 <https://github.com/ansys/pysam-sysml2/pull/118>`_


`0.2.0 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.2.0>`_ - March 16, 2026
=====================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Static approach
          - `#110 <https://github.com/ansys/pysam-sysml2/pull/110>`_

        * - Support inherited elements (#112)
          - `#113 <https://github.com/ansys/pysam-sysml2/pull/113>`_

        * - Add support for transactional mode (#114)
          - `#115 <https://github.com/ansys/pysam-sysml2/pull/115>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump ansys/actions from 10.2.5 to 10.2.7
          - `#109 <https://github.com/ansys/pysam-sysml2/pull/109>`_


  .. tab-item:: Documentation

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Some changes about install, links and parameters in code (#107)
          - `#111 <https://github.com/ansys/pysam-sysml2/pull/111>`_

        * - Fit the documentation for the new release 0.2.0
          - `#117 <https://github.com/ansys/pysam-sysml2/pull/117>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.1.0
          - `#106 <https://github.com/ansys/pysam-sysml2/pull/106>`_


`0.1.0 <https://github.com/ansys/pysam-sysml2/releases/tag/v0.1.0>`_ - March 04, 2026
=====================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Final reviews before releasing
          - `#102 <https://github.com/ansys/pysam-sysml2/pull/102>`_


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Doc deploy permissions
          - `#103 <https://github.com/ansys/pysam-sysml2/pull/103>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump werkzeug from 3.1.5 to 3.1.6
          - `#94 <https://github.com/ansys/pysam-sysml2/pull/94>`_

        * - Bump ansys/actions from 10.2.5 to 10.2.7
          - `#100 <https://github.com/ansys/pysam-sysml2/pull/100>`_

        * - Bump ansys-sphinx-theme[autoapi] from 1.7.1 to 1.7.2
          - `#101 <https://github.com/ansys/pysam-sysml2/pull/101>`_


  .. tab-item:: Miscellaneous

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Updating files from ADO
          - `#28 <https://github.com/ansys/pysam-sysml2/pull/28>`_


.. vale on
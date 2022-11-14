makefile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
package_path := $(shell dirname ${makefile_path})

python = python3
build_path = ${package_path}/target
env_path = ${package_path}/.venv
PYTHON = ${env_path}/bin/python3
name = maze_solver

source_files := $(shell find ${name} -name '*.py')

venv = ${env_path}/venv.stamp
${venv}: pyproject.toml
	[ -d ${env_path} ] || ${python} -m venv ${env_path}
	${PYTHON} -m pip install -e .[dev]
	touch ${env_path}/venv.stamp
	@@echo "To run the virtual environment in your own terminal, run 'source ${env_path}/bin/activate'"

.PHONY: venv
venv: ${venv}

check_format := ${build_path}/black.diff
${check_format}: ${venv} ${source_files}
	@echo '---Checking Formatting---'
	@mkdir -p ${build_path}
	@${PYTHON} -m black --check --diff ${source_files} > ${check_format}

.PHONY: format
format: ${venv}
	@${PYTHON} -m black ${source_files}

.PHONY: clean
clean:
	rm -rf ${build_path}
	rm -rf ${name}.egg-info
	rm -rf ${env_path}

.PHONY: package
package: ${venv} ${source_files}
	${PYTHON} -m build
	mv dist target/
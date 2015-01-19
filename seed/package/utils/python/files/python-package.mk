#
# Copyright (C) 2007 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

PYTHON_VERSION=2.7

PYTHON_DIR:=$(STAGING_DIR)/usr
PYTHON_BIN_DIR:=$(PYTHON_DIR)/bin
PYTHON_INC_DIR:=$(PYTHON_DIR)/include/python$(PYTHON_VERSION)
PYTHON_LIB_DIR:=$(PYTHON_DIR)/lib/python$(PYTHON_VERSION)

HOST_PYTHON_DIR:=$(STAGING_DIR_HOST)
HOST_PYTHON_BIN_DIR:=$(HOST_PYTHON_DIR)/bin
HOST_PYTHON_INC_DIR:=$(HOST_PYTHON_DIR)/include/python$(PYTHON_VERSION)
HOST_PYTHON_LIB_DIR:=$(HOST_PYTHON_DIR)/lib/python$(PYTHON_VERSION)

PYTHON_PKG_DIR:=/usr/lib/python$(PYTHON_VERSION)/site-packages

PYTHON:=python$(PYTHON_VERSION)

HOST_PYTHON_BIN:=$(HOST_PYTHON_BIN_DIR)/$(PYTHON)

HOST_PYTHONPATH:=$(PYTHON_LIB_DIR):$(STAGING_DIR)/$(PYTHON_PKG_DIR)

define HostPython
	(	export PYTHONPATH="$(HOST_PYTHONPATH)"; \
		export PYTHONOPTIMIZE=""; \
		export PYTHONDONTWRITEBYTECODE=1; \
		$(1) \
		$(3) $(2); \
	)
endef

define PyPackage
  $(call shexport,PyPackage/$(1)/filespec)

  define Package/$(1)/install
	@$(SH_FUNC) getvar $$(call shvar,PyPackage/$(1)/filespec) | ( \
		IFS='|'; \
		while read fop fspec fperm; do \
		  if [ "$$$$$$$$fop" = "+" ]; then \
			dpath=`dirname "$$$$$$$$fspec"`; \
			if [ -n "$$$$$$$$fperm" ]; then \
			  dperm="-m$$$$$$$$fperm"; \
			else \
			  dperm=`stat -c "%a" $(PKG_INSTALL_DIR)$$$$$$$$dpath`; \
			fi; \
			mkdir -p $$$$$$$$$dperm $$(1)$$$$$$$$dpath; \
			echo "copying: '$$$$$$$$fspec' to: '$$(1)'"; \
			cp -fpR $(PKG_INSTALL_DIR)$$$$$$$$fspec $$(1)$$$$$$$$dpath/; \
			if [ -n "$$$$$$$$fperm" ]; then \
			  chmod -R $$$$$$$$fperm $$(1)$$$$$$$$fspec; \
			fi; \
		  elif [ "$$$$$$$$fop" = "-" ]; then \
			echo "removing: '$$$$$$$$fspec from: $$(1)'"; \
			rm -fR $$(1)$$$$$$$$fspec; \
		  elif [ "$$$$$$$$fop" = "=" ]; then \
			echo "setting permissions: '$$$$$$$$fperm' on '$$$$$$$$fspec'"; \
			chmod -R $$$$$$$$fperm $$(1)$$$$$$$$fspec; \
		  fi; \
		done; \
	)
	$(call PyPackage/$(1)/install,$$(1))
  endef
endef

# $(1) => build subdir
# $(2) => additional arguments to setup.py
# $(3) => additional variables
define Build/Compile/PyMod
	$(call HostPython, \
		cd $(PKG_BUILD_DIR)/$(strip $(1)); \
		CFLAGS="$(TARGET_CFLAGS)" \
		CPPFLAGS="$(TARGET_CPPFLAGS)" \
		LDFLAGS="$(TARGET_LDFLAGS)" \
		CC="$(TARGET_CC)" \
		LDSHARED="$(TARGET_CC) -shared" \
		$(3) \
		, \
		./setup.py $(2), \
		$(STAGING_DIR)/usr/bin/hostpython \
	)
	find $(PKG_INSTALL_DIR) -name "*\.pyc" -o -name "*\.pyo" | xargs rm -f
endef

define Build/Compile/Host/PyMod
	$(call HostPython, \
		cd $(HOST_BUILD_DIR)/$(strip $(1)); \
		CC="$(HOSTCC)" \
		CFLAGS="$(HOST_CFLAGS)" \
		CPPFLAGS="$(HOST_CPPFLAGS)" \
		LDFLAGS="$(HOST_LDFLAGS)" \
		$(3) \
		, \
		./setup.py $(2), \
		$(HOST_PYTHON_BIN) \
	)
endef

